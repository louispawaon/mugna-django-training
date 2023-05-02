from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from exercises.models import Classification, Book, Author, Publisher

# Create your views here.
def math_view(request, num1, num2, num3=None):
    # Parse the parameters as integers
    try:
        numbers = [int(num1), int(num2)]
        if num3 is not None:
            numbers.append(int(num3))
            total_sum = sum(numbers)
            difference = numbers[0] - numbers[1] - numbers[2]
            product = numbers[0] * numbers[1] * numbers [2]
            quotient = (numbers[0] / numbers[1])/numbers[2]
        else:
            total_sum = sum(numbers)
            difference = numbers[0] - numbers[1]
            product = numbers[0] * numbers[1]
            quotient = numbers[0] / numbers[1]
    except Exception:
        raise ValueError

    context = {
        'numbers': numbers,
        'total_sum': total_sum,
        'difference': difference,
        'product': product,
        'quotient': quotient
    }
    
    return render(request, 'math.html', context)

def valid_date_view(request, YYYY, MM, DD):
    try:

        datetime(int(YYYY), int(MM), int(DD))
        response = "Valid date"
    except ValueError:

        response = "Invalid date"

    context = {
        'date': f"{YYYY}/{MM}/{DD}",
        'validity': response
    }

    return render(request, 'valid_date.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def classification_list(request):
    classifications = Classification.objects.all()
    return render(request, 'classification_list.html', {'classifications': classifications})

def classification_detail(request, classification_id):
    classification = get_object_or_404(Classification, pk=classification_id)
    return render(request, 'classification_detail.html', {'classification': classification})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'publisher_detail.html', {'publisher': publisher})


#Search for publisher and author
#Pages for add, update, delete Books and Publishers
#handle missing fields and wrong data types
