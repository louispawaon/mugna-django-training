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
from django.urls import path
from exercises.views import math_view, valid_date_view
from exercises.views import book_list, book_detail, classification_detail, classification_list, author_detail, author_list


urlpatterns = [
    path("admin/", admin.site.urls),
    path("math/<int:num1>/<int:num2>/",math_view),
    path('math/<int:num1>/<int:num2>/<int:num3>/', math_view),
    path('valid-date/<int:YYYY>/<int:MM>/<int:DD>/', valid_date_view),
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
     path('authors/', author_list, name='author_list'),
    path('authors/<int:author_id>/', author_detail, name='author_detail'),
    path('classification/', classification_list, name='classification_list'),
    path('classification/<int:classification_id>/', classification_detail, name='classification_detail')
]
