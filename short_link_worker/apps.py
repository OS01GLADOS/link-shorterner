from django.apps import AppConfig


class GenerateShortLinkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'short_link_worker'
