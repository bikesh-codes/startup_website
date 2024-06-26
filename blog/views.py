from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.db.models import Count

from .models import Blog, Comment, Reply
# Create your views here.

items_per_page = 5

def blog_index(request):
  blog_list = Blog.objects.annotate(num_comments=Count('comment')).order_by('-created_on')
  paginator = Paginator(blog_list, items_per_page)
  page_number = request.GET.get("page")
  if page_number is None:
    page_number = 1
  blogs = paginator.get_page(page_number)
  context = {'blogs': blogs}
  return render(request, 'blog.html', context)



def blog_details(request, blog_id):
  blog = Blog.objects.get(pk=blog_id)
  paragraphs = blog.blog_desc.split('\n')
  blogs = Blog.objects.all().order_by('-created_on')

  current_index = list(blogs).index(blog)
  if current_index > 0:
    previous_post = blogs[current_index - 1]
  else:
    previous_post = None

  if current_index < len(blogs) - 1:
    next_post = blogs[current_index + 1]
  else:
    next_post = None

  comments = Comment.objects.all().filter(blog_id=blog_id).order_by('-created_on')
  context = {'blog': blog, 'comments': comments, 'blogs': blogs, 'previous_post': previous_post, 'next_post': next_post, 'paragraphs': paragraphs, 'current_blog': blog,}
  return render(request, 'detail.html', context)



def blog_comment(request, blog_id):
  if request.method == "POST":
    posted_by = request.POST["name"]
    comment_desc = request.POST["comment"]
    commenter_email = request.POST["email"]
    commenter_website = request.POST["website"]
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = Comment(posted_by=posted_by, comment_desc=comment_desc, commenter_email=commenter_email, commenter_website=commenter_website, blog=blog)
    comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
  return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
  

def reply_comment(request, blog_id, comment_id):
  if request.method == "POST":
    replied_by = request.POST["reply_name"]
    reply_desc = request.POST["reply_comment"]
    comment = get_object_or_404(Comment, pk=comment_id)
    reply = Reply(comment=comment, replied_by=replied_by, reply_desc=reply_desc)
    reply.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
  return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



