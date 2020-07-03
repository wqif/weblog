from django.contrib import admin

from BlogBackend.custom_site import cus_site
from BlogBackend.settings.base_admin import BaseOwnerAdmin
from apps.comment.models import Comment
from apps.comment.adminforms import CommentAdminForm


# Register your models here.
@admin.register(Comment, site=cus_site)
class CommentAdmin(BaseOwnerAdmin):
    form = CommentAdminForm
    list_display = ('target', 'nickname', 'content', 'website', 'create_time')
