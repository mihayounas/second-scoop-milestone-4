from . import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('menu', views.menu, name='menu'),
    path('reservations', views.ReservationRequest.as_view(), name='reservations'),
    path('reservation_view/', views.ReservationsView.as_view(),
         name='reservations_view'),
    path('reservations_view', views.ReservationsList.as_view(),
         name="reservations_view"),
    path('reservations_view_details/<int:pk>', views.ReservationsViewDetails.as_view(),
         name="reservation_view_details"),
    path('edit/<int:pk>/',
         views.UpdateReservations.as_view(), name='update_reservations'),
    path('delete/<int:pk>/',
         views.DeleteReservations.as_view(), name='delete_reservations'),
    path('thanks', views.thanks, name='thanks'),
    path('post_view', views.PostList.as_view(), name="post_view"),
    path('delete_comment/<int:pk>',
         views.DeleteComment.as_view(), name='delete_comment'),
    path('<slug:slug>', views.PostDetail.as_view(), name="post_detail"),
    path('<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('add_new_post/', views.AddPostView.as_view(), name='add_new_post'),
    path('contact/', views.ContactAdmin.as_view(), name='contact'),
    path('edit_message/<int:pk>/',
         views.UpdateMessages.as_view(), name='update_messages'),
    path('delete_message/<int:pk>/',
         views.DeleteMessages.as_view(), name='delete_messages'),
    path('messages/', views.MessagesList.as_view(), name='message_list'),
    path('update/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/delete', views.DeletePost.as_view(), name='delete_post'),

]
