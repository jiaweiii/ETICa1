from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass
	

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_header = 'Jw Admin'
admin.site.site_title = "Jw Portfolio Portal"