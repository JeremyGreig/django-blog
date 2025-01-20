from django.contrib import admin
from django.urls import path
from .models import Post

# Register your models here.

admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    # other paths...
]