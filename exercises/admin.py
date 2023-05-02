from django.contrib import admin

from exercises.models import (Book, Author, Classification, Publisher)

class BookInLine(admin.TabularInline):
    model = Book
    extra = 3

class BookAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields': ['title', 'authors','publisher', 'publication_date']}),
    ]

class AuthorAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields':['first_name', 'last_name']}),
        ('e-mail', {'fields':['email']})
    ]
    search_fields = ["first_name", "last_name"]
    list_display = ['email']

class PublisherAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['name', 'city', 'country', 'website']})
    ]
    search_fields = ['name', 'city', 'country', 'website']

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Classification)

# Register your models here.
