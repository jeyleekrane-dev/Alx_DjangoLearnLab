from django.urls import path
from .views import AuthorListCreateView,AuthorDetailView,BookListCreateView,BookDetailView

urlpatterns = [
    path('books/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('books/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', BookListCreateView.as_view(), name='book-list-create'),    
    path('authors/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
