from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('create/', views.note_create, name='note_create'),
    path('<int:pk>/edit/', views.note_update, name='note_update'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
