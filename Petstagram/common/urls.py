from django.urls import path, include

from Petstagram.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like')
]
