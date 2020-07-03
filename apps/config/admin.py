from django.contrib import admin

from BlogBackend.custom_site import cus_site
from BlogBackend.settings.base_admin import BaseOwnerAdmin
from apps.config.models import Link, SideBar


# Register your models here.
@admin.register(Link, site=cus_site)
class LinkAdmin(BaseOwnerAdmin):
    fields = ('title', 'href', 'status', 'weight')
    list_display = ('title', 'href', 'status', 'weight', 'create_time')


@admin.register(SideBar, site=cus_site)
class SideBarAdmin(BaseOwnerAdmin):
    fields = ('title', 'display_type', 'content')
    list_display = ('title', 'display_type', 'content', 'create_time')

