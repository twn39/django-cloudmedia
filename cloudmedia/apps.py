from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CloudMediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cloudmedia'
    verbose_name = _('Cloud Media')
