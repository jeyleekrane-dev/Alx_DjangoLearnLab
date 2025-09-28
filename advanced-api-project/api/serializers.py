from serializers import ModelSerializer
from .models import Author, Book
from datetime import datetime
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
class BookSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value < 0 or value > current_year:
            raise serializers.ValidationError(f"Publication year must be between 0 and {current_year}.")
        return value