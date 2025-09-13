from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import get_object_or_404, redirect, render
from django import forms

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'publication_year']

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_books')
	else:
		form = BookForm()
	return render(request, 'bookshelf/create_book.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('list_books')
	else:
		form = BookForm(instance=book)
	return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.delete()
		return redirect('list_books')
	return render(request, 'bookshelf/delete_book.html', {'book': book})
from django.shortcuts import render

# Create your views here.
