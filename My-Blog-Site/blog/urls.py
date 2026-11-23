from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_blog,name='show_blog'),
    path('create_post/', views.post_blog,name='post_blog'),
    path('details_blog/<str:slug>/', views.details_blog, name='details_blog'),
    path('update_blog/<str:slug>/', views.update_blog, name='update_blog'),
    path('delete_blog/<str:slug>/', views.delete_blog, name='delete_blog'),
]
