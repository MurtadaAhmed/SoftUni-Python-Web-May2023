from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create_fruit'),
    path('<int:pk>/details/', views.fruit_details, name='fruit_details'),
    path('<int:pk>/edit/', views.fruit_edit, name='fruit_edit'),
    path('<int:pk>/delete/', views.fruit_delete, name='fruit_delete'),

    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/details/', views.profile_details, name='profile_details'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),

]