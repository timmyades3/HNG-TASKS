from django.urls import path
from . import views


urlpatterns = [
    path('',views.profileList, name='profile-list'),
    path('profile-detail/<str:pk>/',views.profileDetail, name='profile-Detail'),
    path('profile-create',views.profileCreate, name='profile-Create'),
    path('profile-update/<str:pk>/',views.profileUpdate, name='profile-Update'),
    path('profile-delete/<str:pk>/',views.profileDelete, name='profile-Delete'),
]

