from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
import uuid
import hashlib

class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self,email, password=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have a password.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password, **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')

        user = self.create_user( email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True, blank=True, null=True)
    # full_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name= models.CharField(max_length=255, null=True, blank=True)
    dob=models.DateField(null=True,blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    confirm_password = models.CharField(max_length=1000, null=True, blank=True)
    phone_number = models.CharField(max_length=1000, null=True, blank=True)
    student_id = models.CharField(max_length=20, null=True, blank=True)
    gender=models.CharField(max_length=20,null=True,blank=True)
    face_encoding = models.BinaryField(blank=True, null=True)
    company_name=models.TextField(blank=True,null=True)
    company_address=models.TextField(blank=True,null=True)
    company_phone_number=models.TextField(blank=True,null=True)
    company_url=models.TextField(blank=True,null=True)
    profile_image=models.FileField(upload_to='photos',null=True,blank=True)


    
    # Override groups and user_permissions fields
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name="custom_user_groups",  # Unique related_name
    #     blank=True,
    #     verbose_name="groups",
    #     help_text="The groups this user belongs to.",
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name="custom_user_permissions",  # Unique related_name
    #     blank=True,
    #     verbose_name="user permissions",
    #     help_text="Specific permissions for this user.",
    # )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        if self.confirm_password:
            self.confirm_password = hashlib.sha256(str(self.confirm_password).encode()).hexdigest()
        super().save(*args, **kwargs)

    @property
    def name(self):
        return f"{self.full_name}"


class CompanyProfile(models.Model):
    company_phone_number=models.TextField(null=True,blank=True)
    company_name=models.TextField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    company_url=models.TextField(null=True,blank=True)