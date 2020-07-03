from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.utils.translation import gettext as _

from BlogBackend.custom_site import cus_site
from BlogBackend.settings.base_admin import BaseOwnerAdmin

from apps.weblog.models import Tag, Category, Post
from apps.weblog.adminforms import PostAdminForm


# Register your models here.
@admin.register(Category, site=cus_site)
class CategoryAdmin(BaseOwnerAdmin):
    fields = ('name', 'status', 'is_nav')
    list_display = ('name', 'status', 'is_nav', 'create_time', 'post_count')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=cus_site)
class TagAdmin(BaseOwnerAdmin):
    fields = ('name', 'status')
    list_display = ('name', 'status', 'create_time')


class CategoryOwnerFilter(admin.SimpleListFilter):
    '''
    自定义过滤器, 只展示当前用户分类
    '''
    title = '分类过滤器'  # 用于展示标题
    parameter_name = 'owner_category'  # url参数名

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=cus_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = ('title', 'category', 'status', 'create_time')
    list_display_links = ()
    list_filter = (CategoryOwnerFilter,)

    search_fields = ('title', 'category__name')

    filter_horizontal = ('tag',)

    # fields = ('title', 'description', 'content', 'status', 'category', 'tag')
    # _ 将('')里的内容国际化,这样可以让admin里的文字自动随着LANGUAGE_CODE切换中英文
    fieldsets = (
        (_('基础配置'), {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        (_('内容'), {
            'fields': (
                'description', 'content',
            ),
        }),
        (_('额外信息'), {
            'classes': ('collapse',),
            'fields': ('tag',),
        }),
    )


@admin.register(LogEntry, site=cus_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user')
