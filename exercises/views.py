from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from exercises.models import Classification, Book, Author, Publisher
from exercises.forms import PublisherForm, BookForm, RegistrationForm

def is_admin(user):
    return user.is_superuser

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

# Exercise 5
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

@login_required
def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

@login_required
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

# Exercise 6

def author_search(request):
    error = False
    if "q" in request.GET:
        query = request.GET["q"]
        print(query)
        if not query:
            error = True
        else:
            authors = Author.objects.filter(Q(first_name__contains=query)|Q(last_name__contains=query))
            if authors.exists():
                context = {"authors": authors}
                return render(request, "author_search.html", context)
            else:
                error = True
    return render(request, "author_search.html", {"error": error})

def publisher_search(request):
    error = False
    if "q" in request.GET:
        query = request.GET["q"]
        print(query)
        if not query:
            error = True
        else:
            publishers = Publisher.objects.filter(name__icontains=query)
            if publishers.exists():
                context = {"publishers": publishers}
                return render(request, "publisher_search.html", context)
            else:
                error = True
    return render(request, "publisher_search.html", {"error": error})

@user_passes_test(is_admin)
def book_form(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Book.objects.all()})
    return render(request, "book_form.html", {"form": form, "obj": "Book"})

@user_passes_test(is_admin)
def publisher_form(request):
    form = PublisherForm()
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Publisher.objects.all()})
    return render(request, "publisher_form.html", {"form": form, "obj": "Publisher"})

def publisher_update(request, pk=None):
    publisher = get_object_or_404(Publisher, pk=pk)
    form = PublisherForm(instance=publisher)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Publisher.objects.all()})
    return render(request, "publisher_update.html", {"form": form, "obj": "Publisher"})

def book_update(request, pk=None):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return render(request, "crud_results.html", {"results": Book.objects.all()})
    return render(request, "book_update.html", {"form": form, "obj": "Book"})

def publisher_delete(request, pk=None):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return render(request, "crud_results.html", {"results": Publisher.objects.all()})
    return render(request, "publisher_delete.html", {"obj": "Publisher"})

def book_delete(request, pk=None):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return render(request, "crud_results.html", {"results": Book.objects.all()})
    return render(request, "book_delete.html", {"obj": "Book"})

# Exercise 7

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            return render(request, "home.html")
    else:
        form = RegistrationForm()
    
    return render(request, "register.html", {"form": form})

def home(request):
    return render( request, "home.html")
        
