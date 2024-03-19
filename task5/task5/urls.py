"""
URL configuration for task5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostListWithComments.as_view(), name='post-list-with-comments'),
    path('filtered-posts/', FilteredPostList.as_view(), name='filtered-post-list'),
    path('posts-by-recent-comments/', PostsByRecentComments.as_view(), name='posts-by-recent-comments'),
    path('posts-by-created-at/', PostsByCreatedAt.as_view(), name='posts-by-created-at'),
    path('delete-posts-with-no-comments/<int:pk>/', DeletePostWithNoComments.as_view(), name='delete-posts-with-no-comments'),
]
