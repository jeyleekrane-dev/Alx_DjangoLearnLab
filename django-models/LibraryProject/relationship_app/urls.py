from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library_detail'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('register/', views.register, name='register'),
]
