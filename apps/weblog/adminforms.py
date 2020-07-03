# coding=utf-8

# @Author: Qifeng Wen 
# @File: adminforms.py 
# @Contact: wenqifeng97@163.com
# @Time: 2020/07/03 09:46:06  
# @Software: PyCharm


from django import forms


class PostAdminForm(forms.ModelForm):
    '''
    自定义表单样式
    '''
    description = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
