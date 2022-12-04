from django import template
from blog.models import Post 
register = template.Library()


@register.inclusion_tag('website/web-latestposts.html')
def Sixlatestposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    return {'posts':posts}
