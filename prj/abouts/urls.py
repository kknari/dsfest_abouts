from django.urls import path, include

from . import views


urlpatterns = [
    path('abouts/', views.PostList.as_view()),
]