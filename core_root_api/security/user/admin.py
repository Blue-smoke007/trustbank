from django.contrib import admin
from core_root_api.security.user.models import User,CompanyProfile
# Register your models here.

admin.site.register(User)
admin.site.register(CompanyProfile)