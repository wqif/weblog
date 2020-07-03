from django.contrib.auth.models import User
from django.db import models

from apps.weblog.models import Post


# Create your models here.
class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='评论目标文章')
    content = models.CharField(max_length=2000, verbose_name='评论内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    status = models.PositiveIntegerField(default=STATUS_ITEMS, choices=STATUS_ITEMS, verbose_name='评论状态')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='评论用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return str(self.id) + "-" + str(self.content)

    class Meta:
        verbose_name = verbose_name_plural = '评论信息'
