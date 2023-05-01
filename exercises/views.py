from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from exercises.models import Classification, Book, Author

# Create your views here.
def math_view(request, num1, num2, num3=None):
    # Parse the parameters as integers
    try:
        numbers = [int(num1), int(num2)]
        if num3:
            numbers.append(int(num3))
        else:
            numbers.append(0)

        # Compute the results
        total_sum = sum(numbers)
        difference = numbers[0] - numbers[1] - numbers[2]
        product = numbers[0] * numbers[1] * numbers [2]
        quotient = (numbers[0] / numbers[1])/numbers[2]

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
    context={
        'books': books
    }
    return render(request, 'book_list.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context={
        'book':book
    }
    return render(request, 'book_detail.html', context)

def author_list(request):
    author = Author.objects.all()
    context={
        'authors': author
    }
    return render(request, 'author_list.html', context)

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(author=author)
    context={
        'author':author,
        'books':books
    }
    return render(request, 'author_detail.html', context)

def classification_list(request):
    classifications = Classification.objects.all()
    context={
        'classifications':classifications
    }
    return render(request, 'classification_list.html', context)

def classification_detail(request, classification_id):
    classification = Classification.objects.get(pk=classification_id)
    books = Book.objects.filter(classification=classification)
    context={
        'classification':classification,
        'books':books
    }
    return render(request, 'classification_detail.html', context)
