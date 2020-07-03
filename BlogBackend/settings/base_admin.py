# coding=utf-8

# @Author: Qifeng Wen 
# @File: base_admin.py 
# @Contact: wenqifeng97@163.com
# @Time: 2020/07/03 11:10:29  
# @Software: PyCharm
from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    '''
    1. 保存式自动添加当前用户
    2. 过滤掉非当前用户数据
    '''
    exclude = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super(BaseOwnerAdmin, self).get_queryset(request).filter(owner=request.user)
