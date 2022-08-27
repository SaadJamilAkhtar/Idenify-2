from django.apps import AppConfig


class BaseAdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base_admin"
