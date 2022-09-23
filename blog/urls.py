from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu', views.menu, name='menu'),
    path('reservations', views.ReservationRequest.as_view(), name='reservations'),
    path('thanks', views.thanks, name='thanks'),
    path('post_view', views.PostList.as_view(), name="post_view"),
    path('<slug:slug>', views.PostDetail.as_view(), name="post_detail"),
    path('<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('add_new_post/', views.AddPostView.as_view(), name='add_new_post'),
    path('contact/', views.ContactAdmin.as_view(), name='contact')
]
