from django.contrib import admin
from .models import Post
from django.urls import path


# Register your models here.

admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    # other paths...
]