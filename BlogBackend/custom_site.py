# coding=utf-8

# @Author: Qifeng Wen 
# @File: custom_site.py 
# @Contact: wenqifeng97@163.com
# @Time: 2020/07/03 10:18:06  
# @Software: PyCharm

from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Weblog'
    site_title = 'Weblog管理后台'
    index_title = '首页'

cus_site = CustomSite(name='custom_admin')
