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

    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        # QuerySet的懒惰性在使用到数据时才会访问数据库,避免两次访问数据库, 选择一次查询在内存中将数据拆分
        for category in categories:
            if category.is_nav:
                nav_categories.append(category)
            else:
                normal_categories.append(category)
        return {'navs': nav_categories, 'categories': normal_categories}

    def __str__(self):
        return str(self.id) + "-" + str(self.name)

    class Meta:
        verbose_name = verbose_name_plural = '分类信息'


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

    def __str__(self):
        return str(self.id) + "-" + str(self.name)

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
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    pv = models.PositiveIntegerField(default=1, verbose_name='访问量')
    uv = models.PositiveIntegerField(default=1)

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv').only('pv', 'uv')

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        except Category.DoesNotExist:
            category = None
            post_list = []
        return post_list, category

    @classmethod
    def latest_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL)

    def __str__(self):
        return str(self.id) + "-" + str(self.title)

    class Meta:
        verbose_name = verbose_name_plural = '文章信息'
        ordering = ['-id']
