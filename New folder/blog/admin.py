from django.contrib import admin

from blog.models import Post , Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author', 'counted_views','updated_date' , 'status' , 'created_date','published_date' )
    list_filter =  ['status','author']
    #ordering = ['-created_date']
    search_fields = ['title','content']
    #pass
    

admin.site.register(Category)
admin.site.register(Post , PostAdmin)
