from django.shortcuts import render , get_object_or_404
from blog.models import Post
import datetime
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
# Create your views here.

def blog_view(requests , cat_name = None , author_username = None):
    #posts = Post.objects.filter(status = 1)
    posts = Post.objects.filter(published_date__lte = datetime.datetime.now())
    if cat_name:
        posts = posts.filter(category__name = cat_name)
    if author_username:
        posts = posts.filter(author__username = author_username)
        
    posts = Paginator(posts,3)
    
    try:
        page_number = requests.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
                        
    context = {'posts':posts}
    return render(requests , 'blog/blog-home.html',context)



def blog_single(requests,pid):
    post = get_object_or_404(Post ,pk=pid , status=1)
    if post:
        post.counted_views = post.counted_views +1
        post.save()
    
    context = {'post':post }
    return render(requests, 'blog/blog-single.html',context)



def test(requests):
    #post = Post.objects.get(id = pid)
    #post = get_object_or_404(Post ,pk=pid)
    #context = {'post':post}
    return render(requests , 'test.html')


#def blog_category(requests,cat_name):
 #   posts = Post.objects.filter(status=1)
 #   posts = posts.filter(category__name = cat_name)
  #  context = {'posts':posts }
 #   return render(requests, 'blog/blog-home.html',context)
 
def blog_search(requests):
    posts = Post.objects.filter(status=1)
    
    if requests.method == 'GET':
        posts = posts.filter(content__contains=requests.GET.get('s'))
    context = {'posts':posts}
    return render(requests , 'blog/blog-home.html',context)
        