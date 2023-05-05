import requests
from django.core.management.base import BaseCommand
from exercises.models import Book, Author


class Command(BaseCommand):
    help = "Imports books and authors from the Gutendex API endpoint"

    def handle(self, *args, **options):
        url = "http://gutendex.com/books/"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            for result in data["results"]:
                title = (result.get("title"),)
                book, _ = Book.objects.get_or_create(title=title)
                self.stdout.write(f"Adding book {title} to the database ...")

                for author_name in result["authors"]:
                    last_name, first_name = author_name.get("name").split(",")
                    author, _ = Author.objects.get_or_create(
                        last_name=last_name, first_name=first_name
                    )
                    book.authors.add(author)

                    self.stdout.write(
                        f"Adding author {last_name}, {first_name} to the database ..."
                    )

        else:
            self.stdout.write(self.style.ERROR("Failed to import books and authors"))
