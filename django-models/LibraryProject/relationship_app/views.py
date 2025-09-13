from .models import Library
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login

# User registration view


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Function-based view to list all books


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Create your views here.


class Newview(DetailView):
    pass
