from django.contrib import admin
from blog.models import blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog', 'date')

admin.site.register(blog, BlogAdmin)

# Register your models here.
