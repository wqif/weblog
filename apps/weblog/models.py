from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=50, verbose_name='分类名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='分类状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章分类信息'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name='标签名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='标签状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签信息'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )
    # id = models.AutoField(primary_key=True, verbose_name=u'文章ID')
    title = models.CharField(max_length=32, verbose_name='文章标题')
    description = models.CharField(max_length=256, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章正文', help_text='正文必须为MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='文章状态')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='文章分类')
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, verbose_name='文章标签')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章信息'
        ordering = ['-id']
