from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu', views.menu, name='menu'),
    path('reservations', views.reservation, name='reservations'),
    path('thanks', views.thanks, name='thanks'),
    path('post_view', views.PostList.as_view(), name="post_view"),
    path('<slug:slug>', views.PostDetail.as_view(), name="post_detail"),
    path('<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('add_post/', views.create_post, name="add_post"),
    path('new_posts/', views.NewPostList.as_view(), name='new_posts')
]
