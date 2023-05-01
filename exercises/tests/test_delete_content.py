from exercises.models import Book, Classification, Author

Book.objects.all().delete()
Classification.objects.all().delete()
Author.objects.all().delete()