from django.contrib import admin
from .models import MediaGroup, Media
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Media info'), {'fields': (
            'title', 'caption', 'file', 'description', 'filetype',
            'uploader', 'media_group', 'file_name', 'file_preview'
        )}),
        (_('Important dates'), {'fields': ('created_at', 'updated_at')})
    )
    list_display = ['title', 'caption', 'file', 'file_thumbnail', 'media_group', 'filetype', 'file_size', 'created_at']
    list_filter = ['filetype', 'created_at']
    readonly_fields = ['file_name', 'file_preview']

    @admin.display(description=_('file name'))
    def file_name(self, instance) -> str:
        return instance.file.name

    @admin.display(description=_('preview'))
    def file_preview(self, instance):
        if instance.filetype == 0:
            img = u'<img width=400 src="%s" />' % escape(instance.file.url)
            return mark_safe(img)
        return instance.file.url

    @admin.display(description=_('thumbnail'))
    def file_thumbnail(self, instance):
        if instance.filetype == 0:
            img = u'<img width=75 src="%s" />' % escape(instance.file.url)
            return mark_safe(img)
        return instance.file.url

    @admin.display(description=_('size'))
    def file_size(self, instance):
        return u'%s KB' % (int(instance.file.size) / 1000)


@admin.register(MediaGroup)
class MediaGroupAdmin(admin.ModelAdmin):
    fields = ['caption', 'name', 'description', 'creator', 'created_at', 'updated_at']
    list_display = ['caption', 'name', 'creator', 'created_at', 'updated_at']
    list_filter = ['created_at']

