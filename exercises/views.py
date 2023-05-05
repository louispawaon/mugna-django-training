from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from exercises.models import Classification, Book, Author, Publisher
from exercises.forms import PublisherForm, BookForm, RegistrationForm, AuthorForm


def is_admin(user):
    return user.is_superuser


def user_logout(request):
    if "search_history" in request.session:
        del request.session["search_history"]
    logout(request)
    return HttpResponseRedirect(reverse("home"))


# Create your views here.
def math_view(request, num1, num2, num3=None):
    # Parse the parameters as integers
    try:
        numbers = [int(num1), int(num2)]
        if num3 is not None:
            numbers.append(int(num3))
            total_sum = sum(numbers)
            difference = numbers[0] - numbers[1] - numbers[2]
            product = numbers[0] * numbers[1] * numbers[2]
            quotient = (numbers[0] / numbers[1]) / numbers[2]
        else:
            total_sum = sum(numbers)
            difference = numbers[0] - numbers[1]
            product = numbers[0] * numbers[1]
            quotient = numbers[0] / numbers[1]
    except Exception:
        raise ValueError

    context = {
        "numbers": numbers,
        "total_sum": total_sum,
        "difference": difference,
        "product": product,
        "quotient": quotient,
    }

    return render(request, "math.html", context)


def valid_date_view(request, YYYY, MM, DD):
    try:
        datetime(int(YYYY), int(MM), int(DD))
        response = "Valid date"
    except ValueError:
        response = "Invalid date"

    context = {"date": f"{YYYY}/{MM}/{DD}", "validity": response}

    return render(request, "valid_date.html", context)


# Exercise 5
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "book_detail.html", {"book": book})


def author_list(request):
    authors = Author.objects.all()
    return render(request, "author_list.html", {"authors": authors})


@login_required
def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "author_detail.html", {"author": author})


@login_required
def classification_list(request):
    classifications = Classification.objects.all()
    return render(
        request, "classification_list.html", {"classifications": classifications}
    )


def classification_detail(request, classification_id):
    classification = get_object_or_404(Classification, pk=classification_id)
    return render(
        request, "classification_detail.html", {"classification": classification}
    )


def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, "publisher_list.html", {"publishers": publishers})


def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, "publisher_detail.html", {"publisher": publisher})


# Exercise 6


# def author_search(request):
#     error = False
#     if "q" in request.GET:
#         query = request.GET["q"]
#         print(query)
#         if not query:
#             error = True
#         else:
#             authors = Author.objects.filter(Q(first_name__contains=query)|Q(last_name__contains=query))
#             if authors.exists():
#                 context = {"authors": authors}
#                 return render(request, "author_search.html", context)
#             else:
#                 error = True
#     return render(request, "author_search.html", {"error": error})

# def publisher_search(request):
#     error = False
#     if "q" in request.GET:
#         query = request.GET["q"]
#         print(query)
#         if not query:
#             error = True
#         else:
#             publishers = Publisher.objects.filter(name__icontains=query)
#             if publishers.exists():
#                 context = {"publishers": publishers}
#                 return render(request, "publisher_search.html", context)
#             else:
#                 error = True
#     return render(request, "publisher_search.html", {"error": error})


# @user_passes_test(is_admin)
# def book_form(request):
#     form = BookForm()
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, "crud_results.html", {"results": Book.objects.all()})
#     return render(request, "book_form.html", {"form": form, "obj": "Book"})

# @user_passes_test(is_admin)
# def publisher_form(request):
#     form = PublisherForm()
#     if request.method == "POST":
#         form = PublisherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, "crud_results.html", {"results": Publisher.objects.all()})
#     return render(request, "publisher_form.html", {"form": form, "obj": "Publisher"})

# def publisher_update(request, pk=None):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     form = PublisherForm(instance=publisher)
#     if request.method == "POST":
#         form = PublisherForm(request.POST, instance=publisher)
#         if form.is_valid():
#             form.save()
#             return render(request, "crud_results.html", {"results": Publisher.objects.all()})
#     return render(request, "publisher_update.html", {"form": form, "obj": "Publisher"})

# def book_update(request, pk=None):
#     book = get_object_or_404(Book, pk=pk)
#     form = BookForm(instance=book)
#     if request.method == "POST":
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return render(request, "crud_results.html", {"results": Book.objects.all()})
#     return render(request, "book_update.html", {"form": form, "obj": "Book"})

# def publisher_delete(request, pk=None):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     if request.method == "POST":
#         publisher.delete()
#         return render(request, "crud_results.html", {"results": Publisher.objects.all()})
#     return render(request, "publisher_delete.html", {"obj": "Publisher"})

# def book_delete(request, pk=None):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return render(request, "crud_results.html", {"results": Book.objects.all()})
#     return render(request, "book_delete.html", {"obj": "Book"})

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
    return render(request, "home.html")


# Exercise 8


def author_form(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request, "crud_results.html", {"results": Author.objects.all()}
            )
    return render(request, "author_form.html", {"form": form, "obj": "Author"})


def author_update(request, pk=None):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(instance=author)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return render(
                request, "crud_results.html", {"results": Author.objects.all()}
            )
    return render(request, "author_update.html", {"form": form, "obj": "Author"})


def author_delete(request, pk=None):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return render(request, "crud_results.html", {"results": Author.objects.all()})
    return render(request, "author_delete.html", {"obj": "Author"})


# Exercise 9
class SearchPublisherView(ListView):
    model = Publisher
    context_object_name = "publishers"
    template_name = "publisher_search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            publisher_search_history = self.request.session.get(
                "publisher_search_history", []
            )
            publisher_search_history.append(query)
            self.request.session["publisher_search_history"] = publisher_search_history
            return Publisher.objects.filter(name__icontains=query)
        else:
            return Publisher.objects.all()


class SearchAuthorView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "author_search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            author_search_history = self.request.session.get(
                "author_search_history", []
            )
            author_search_history.append(query)
            self.request.session["author_search_history"] = author_search_history
            return Author.objects.filter(
                Q(first_name__contains=query) | Q(last_name__contains=query)
            )
        else:
            return Author.objects.all()


class CreateBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_form.html"

    @user_passes_test(is_admin)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("book_list"))
        return render(request, "book_form.html", {"form": form, "obj": "Book"})


class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    context_object_name = "books"
    template_name = "book_update.html"

    @user_passes_test(is_admin)
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse("book_detail", args=[self.object.pk]))


class DeleteBookView(DeleteView):
    model = Book
    template_name = "book_delete.html"

    @user_passes_test(is_admin)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse("book_list"))


class CreatePublisherView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = "publisher_form.html"

    @user_passes_test(is_admin)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("publisher_list"))
        return render(
            request, "publisher_form.html", {"form": form, "obj": "Publisher"}
        )


class UpdatePublisherView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    context_object_name = "publishers"
    template_name = "publisher_update.html"

    @user_passes_test(is_admin)
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse("publisher_detail", args=[self.object.pk]))


class DeletePublisherView(DeleteView):
    model = Publisher
    template_name = "publisher_delete.html"

    @user_passes_test(is_admin)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse("publisher_list"))


class PublisherSearchHistory(ListView):
    template_name = "search_history.html"
    context_object_name = "publisher_search_history"

    def get_queryset(self):
        if self.request.session.get("publisher_search_history"):
            return self.request.session["publisher_search_history"]


class AuthorSearchHistory(ListView):
    template_name = "search_history.html"
    context_object_name = "author_search_history"

    def get_queryset(self):
        if self.request.session.get("author_search_history"):
            return self.request.session["author_search_history"]
