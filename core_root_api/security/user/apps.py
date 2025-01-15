from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_root_api.security.user'
    label= 'core_root_api_security_user'
