# coding=utf-8

# @Author: Qifeng Wen 
# @File: adminforms.py 
# @Contact: wenqifeng97@163.com
# @Time: 2020/07/03 09:49:24  
# @Software: PyCharm


from django import forms


class CommentAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='评论内容', required=False)
