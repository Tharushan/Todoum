from django.apps import AppConfig


class TodoumAdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todoum.todoum_admin"
    label = "todoum_admin"
    verbose_name = "Todoum Admin"
