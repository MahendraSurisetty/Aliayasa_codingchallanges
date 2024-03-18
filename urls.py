"""
URL configuration for project4 project.

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
     path('list-posts/', ListPostsAPIView.as_view(), name='list-posts'),
    path('filter-posts/', FilteredPostsAPIView.as_view(), name='filter-posts'),
    path('recent-comments-posts/', RecentCommentsPostsAPIView.as_view(), name='recent-comments-posts'),
    path('created-at-posts/', CreatedAtPostsAPIView.as_view(), name='created-at-posts'),
    path('delete-empty-posts/', DeleteEmptyPostsAPIView.as_view(), name='delete-empty-posts'),
]
