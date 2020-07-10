from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView

from apps.weblog.models import Post, Tag, Category
from apps.config.models import SideBar


# Create your views here.


class IndexView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 3  # 设置每页展示记录条数
    context_object_name = 'post_list'  # 模板反向解析url的name
    template_name = 'weblog/list.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())

        return context

    def get_queryset(self):
        '''重写get_queryset 根据category过滤'''
        category_id = self.kwargs.get('category_id')
        filters = dict()
        if category_id:
            filters.update({'category_id': category_id})
        return super(IndexView, self).get_queryset().filter(**filters)


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })

        return context

class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })

        return context

    def get_queryset(self):
        '''重写get_queryset 根据tag过滤'''
        tag_id = self.kwargs.get('tag_id')
        filters = dict()
        if tag_id:
            filters.update({'tag__id': tag_id})
        return super(TagView, self).get_queryset().filter(**filters)


class PostDetailView(IndexView):
    queryset = Post.latest_posts()
    template_name = 'weblog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None
#     if tag_id:
#         posts, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         posts, category = Post.get_by_category(category_id)
#     else:
#         posts = Post.latest_posts()
#
#     context = {'posts': posts, 'category': category, 'tag': tag, 'sidebars': SideBar.get_all()}
#     context.update(Category.get_navs())
#     return render(request, 'weblog/list.html', context=context)


# def post_detail(request, post_id=None):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#
#     context = {'post': post, 'sidebars': SideBar.get_all()}
#     context.update(Category.get_navs())
#     return render(request, 'weblog/detail.html', context=context)


def links(request):
    return HttpResponse('links')
