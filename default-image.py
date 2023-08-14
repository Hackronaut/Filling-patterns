from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings

from .models import YourModel

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            default_image_url = settings.STATIC_URL + 'img/adv.png'
            return format_html('<img src="{}" width="50" height="50" />'.format(default_image_url))

    image_thumbnail.short_description = 'Thumbnail'
