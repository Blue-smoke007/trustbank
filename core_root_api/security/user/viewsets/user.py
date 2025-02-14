from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from core_root_api.security.user.serializers.user import UserSerializer
from core_root_api.security.user.models import User

class UserViewset(viewsets.ModelViewSet):
    http_method_names=['patch','get']
    permission_classes=[AllowAny,]
    serializer_class=UserSerializer
    

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.exclude(is_superuser=True)
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj=User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj

