from django.db import models
import django.utils.timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class MediaGroup(models.Model):
    name = models.CharField(_('name'), max_length=255, default='')
    caption = models.CharField(_('caption'), max_length=255, default='')
    description = models.CharField(_('description'), max_length=255, default='')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('creator'))
    created_at = models.DateTimeField(_('created at'), default=django.utils.timezone.now)
    updated_at = models.DateTimeField(_('updated at'), default=django.utils.timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Media Group')
        verbose_name_plural = _('Media Group')


class Media(models.Model):
    IMAGE = 0
    VIDEO = 1
    AUDIO = 2
    DOC = 3
    PDF = 4
    ARCHIVE = 5
    OTHER = 6

    MEDIA_TYPE_CHOICES = [
        (IMAGE, _('image')),
        (VIDEO, _('video')),
        (AUDIO, _('audio')),
        (DOC, _('doc')),
        (PDF, _('pdf')),
        (ARCHIVE, _('archive')),
        (OTHER, _('other'))
    ]

    title = models.CharField(_('title'), max_length=255, default='')
    caption = models.CharField(_('caption'), max_length=255, default='')
    file = models.FileField(_('file'), default='')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('uploader'))
    media_group = models.ForeignKey(MediaGroup, on_delete=models.CASCADE, verbose_name=_('media group'))
    description = models.CharField(_('description'), max_length=255, default='')
    format = models.CharField(_('file format'), max_length=255, default='')
    filetype = models.IntegerField(_('file type'), choices=MEDIA_TYPE_CHOICES, default=IMAGE)
    created_at = models.DateTimeField(_('created at'), default=django.utils.timezone.now)
    updated_at = models.DateTimeField(_('updated at'), default=django.utils.timezone.now)

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')
        ordering = ['created_at']

    def __str__(self):
        return self.title


