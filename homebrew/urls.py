from django.contrib import admin
from django.urls import path
from . import views


app_name = 'homebrew'
urlpatterns = [
    path('new_weapon/', views.new_weapon, name= 'new_weapon'),
    path('new_armor/', views.new_armor, name= 'new_armor'),
    path('new_item/', views.new_item, name= 'new_item'),
    path('new_career/', views.new_career, name= 'new_career'),
    path('new_homebrew/', views.new_homebrew, name= 'new_homebrew'),
    path('browse/', views.browse, name='browse'),
    path('select/', views.select, name='select'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/edit_weapon/', views.edit_weapon, name='edit_weapon'),
    path('<int:pk>/delete/', views.delete, name='delete')
    ]
