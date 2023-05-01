from exercises.models import Book, Classification, Author

# Create some classifications
c1 = Classification.objects.create(code='001', name='Fiction', description='Fiction books')
c2 = Classification.objects.create(code='002', name='Non-Fiction', description='Non-fiction books')

# Create some authors
a1 = Author.objects.create(name='Juan dela Cruz')
a2 = Author.objects.create(name='Minerva Cortez')

# Create some books
Book.objects.create(title='Book 1', author=a1, classification=c1)
Book.objects.create(title='Book 2', author=a2, classification=c1)
Book.objects.create(title='Book 3', author=a1, classification=c2)