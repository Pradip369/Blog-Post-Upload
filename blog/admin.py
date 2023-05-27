from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ["title","disc",'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
