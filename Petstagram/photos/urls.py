from django.urls import path, include
from Petstagram.photos import views

urlpatterns = [
    path('add/', views.PhotoAddPageView.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details_page, name='photo-details'),
        path('edit/', views.PhotoEditPageView.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
    ]))
]
