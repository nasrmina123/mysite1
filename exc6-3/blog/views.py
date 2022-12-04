from django.shortcuts import render , get_object_or_404
from blog.models import Post
import datetime
# Create your views here.

def blog_view(requests):
    #posts = Post.objects.filter(status = 1)
    posts = Post.objects.filter(published_date__lte = datetime.datetime.now())
    context = {'posts':posts}
    return render(requests , 'blog/blog-home.html',context)



def blog_single(requests,pid):
    post = get_object_or_404(Post ,pk=pid , status=1)
    if post:
        post.counted_views = post.counted_views +1
        post.save()
    
    #posts = Post.objects.all()    
    #previous_post = get_object_or_404(Post ,pk__lt = pid , status=1) 
    
    #next_post = get_object_or_404(Post , pk__lt =pid , status=1)
    
    context = {'post':post }
    return render(requests, 'blog/blog-single.html',context)



def test(requests , pid):
    post = Post.objects.get(id = pid)
    #post = get_object_or_404(Post ,pk=pid)
    context = {'post':post}
    return render(requests , 'test.html',context)