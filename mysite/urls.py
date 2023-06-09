"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from exercises.views import math_view, valid_date_view
from exercises.views import (
    book_list,
    book_detail,
    classification_detail,
    classification_list,
    author_detail,
    author_list,
    publisher_detail,
    publisher_list,
    register,
    home,
    user_logout,
    author_delete,
    author_form,
    author_update,
)
from exercises.views import (
    SearchPublisherView,
    SearchAuthorView,
    CreateBookView,
    UpdateBookView,
    DeleteBookView,
    CreatePublisherView,
    UpdatePublisherView,
    DeletePublisherView,
    PublisherSearchHistory,
    AuthorSearchHistory,
)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("math/<int:num1>/<int:num2>/", math_view),
    path("math/<int:num1>/<int:num2>/<int:num3>/", math_view),
    path("valid-date/<int:YYYY>/<int:MM>/<int:DD>/", valid_date_view),
    path("books/", book_list, name="book_list"),
    path("books/<int:book_id>/", book_detail, name="book_detail"),
    path("authors/", author_list, name="author_list"),
    path("authors/<int:author_id>/", author_detail, name="author_detail"),
    path("classification/", classification_list, name="classification_list"),
    path(
        "classification/<int:classification_id>/",
        classification_detail,
        name="classification_detail",
    ),
    path("publishers/", publisher_list, name="publisher_list"),
    path("publishers/<int:publisher_id>/", publisher_detail, name="publisher_detail"),
    # path('authors/search/', author_search, name="author_search"),
    # path('publishers/search/', publisher_search, name="publisher_search"),
    # path('books/add/', book_form, name='book_form'),
    # path('publishers/add/', publisher_form, name='publisher_form'),
    # path('publishers/update/<int:pk>/', publisher_update, name='publisher_update'),
    # path('books/update/<int:pk>/', book_update, name='book_update'),
    # path('publishers/delete/<int:pk>/', publisher_delete, name='publisher_delete'),
    # path('books/delete/<int:pk>/', book_delete, name='book_delete'),
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("user_logout/", user_logout, name="user_logout"),
    path("authors/add/", author_form, name="author_form"),
    path("authors/update/<int:pk>/", author_update, name="author_update"),
    path("authors/delete/<int:pk>/", author_delete, name="author_delete"),
    # Exercise 9
    path("publishers/search/", SearchPublisherView.as_view(), name="publisher_search"),
    path("authors/search/", SearchAuthorView.as_view(), name="author_search"),
    path("books/add/", CreateBookView.as_view(), name="book_form"),
    path("books/update/<int:pk>/", UpdateBookView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", DeleteBookView.as_view(), name="book_delete"),
    path("publishers/add/", CreatePublisherView.as_view(), name="publisher_form"),
    path(
        "publishers/update/<int:pk>/",
        UpdatePublisherView.as_view(),
        name="publisher_update",
    ),
    path(
        "publishers/delete/<int:pk>/",
        DeletePublisherView.as_view(),
        name="publisher_delete",
    ),
    path(
        "search_history/",
        PublisherSearchHistory.as_view(),
        name="search_history",
    ),
    path(
        "search_history/",
        AuthorSearchHistory.as_view(),
        name="search_history",
    ),
]
