from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
print("Books by Author:", list(books_by_author))

library_name = "Library Name"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in Library:", list(books_in_library))

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for Library:", librarian)
