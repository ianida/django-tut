from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
# This code registers the Post model with the Django admin site, allowing it to be managed through the admin interface.
