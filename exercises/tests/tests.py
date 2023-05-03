from django.test import TestCase, Client
from django.urls import reverse
from exercises.models import Author, Book, Publisher, Classification
from django.contrib.auth.models import User
from datetime import datetime

# Author and Publisher Search
class AuthorSearchViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.author1 = Author.objects.create(first_name="John", last_name="Doe", email="johndoe@example.com")
        self.author2 = Author.objects.create(first_name="Jane", last_name="Doe", email="janedoe@example.com")
        self.publisher1 = Publisher.objects.create(name="Publisher 1", address="Address 1", city="City 1", state_province="State/Province 1", country="Country 1", website="http://www.publisher1.com/")
        self.book1 = Book.objects.create(title="Book 1", publisher=self.publisher1, publication_date="2021-01-01")
        self.book1.authors.add(self.author1, self.author2)

    def test_author_search_view_with_results(self):
        response = self.client.get(reverse("author_search"), {"q": "John"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertNotContains(response, "Jane Doe")

    def test_author_search_view_without_results(self):
        response = self.client.get(reverse("author_search"), {"q": "Foo"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "John Doe")
        self.assertNotContains(response, "Jane Doe")
        self.assertContains(response, "No authors found.")

class PublisherSearchViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Publisher.objects.create(name="Publisher A", address="Address A", city="City A", state_province="State A", country="Country A", website="http://www.publisherA.com")
        Publisher.objects.create(name="Publisher B", address="Address B", city="City B", state_province="State B", country="Country B", website="http://www.publisherB.com")

    def test_search_view_with_results(self):
        response = self.client.get(reverse('publisher_search'), {'q': 'Publisher A'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Publisher A')

    def test_publisher_search_view_with_no_results(self):
        response = self.client.get(reverse('publisher_search'), {'q': 'Publisher C'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No publishers found.')

# Login and Logout
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='johndoe', email='johndoe@example.com', password='secret')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': 'johndoe', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': 'johndoe', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

class LogoutViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)

# Author, Publisher, Book, Classification Detail
class AuthorDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(first_name="John", last_name="Doe", email="johndoe@example.com")
        self.url = reverse('author_detail', args=[self.author.id])

    def test_author_detail_view_authenticated(self):
        # Authenticate the client with a user
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(user)

        response = self.client.get(reverse("author_detail", kwargs={"author_id": self.author.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.first_name)
        self.assertContains(response, self.author.last_name)

    def test_author_detail_view_unauthenticated(self):
        response = self.client.get(reverse("author_detail", kwargs={"author_id": self.author.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/authors/{self.author.id}/')

class BookDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.publisher = Publisher.objects.create(
            name="Publisher A",
            address="Matina",
            city="Davao City",
            state_province="Davao del Sur",
            country="PH",
            website="http://www.publisher-a.com"
        )
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com"
        )
        self.book = Book.objects.create(
            title="Book 1",
            publisher=self.publisher,
            publication_date="2021-01-01"
        )
        self.book.authors.add(self.author)

    def test_book_detail_view_with_existing_book(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_login(user)
        response = self.client.get(reverse("book_detail", args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.publisher.name)
        self.assertContains(response, self.author.first_name)
        self.assertContains(response, self.author.last_name)

    def test_book_detail_view_with_nonexistent_book(self):
        nonexistent_book_id = self.book.id + 1
        response = self.client.get(reverse("book_detail", args=[nonexistent_book_id]))
        self.assertEqual(response.status_code, 302)

class PublisherDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.publisher = Publisher.objects.create(name="Publisher A", address="Baliok", city="Davao City", state_province="Davao del Sur", country="PH", website="http://www.publisher-a.com")
        self.author1 = Author.objects.create(first_name="John", last_name="Doe", email="johndoe@example.com")
        self.author2 = Author.objects.create(first_name="Jane", last_name="Doe", email="janedoe@example.com")
        self.book = Book.objects.create(title="Book 1", publisher=self.publisher, publication_date="2021-01-01")
        self.book.authors.add(self.author1, self.author2)
        self.url = reverse('book_detail', args=[self.book.id])

    def test_publisher_detail_view_with_valid_publisher(self):
        response = self.client.get(reverse('publisher_detail', args=[self.publisher.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.publisher.name)
        self.assertContains(response, self.publisher.address)
        self.assertContains(response, self.publisher.city)
        self.assertContains(response, self.publisher.state_province)
        self.assertContains(response, self.publisher.country)
        self.assertContains(response, self.publisher.website)
        self.assertContains(response, self.book.title)

class ClassificationDetailViewTestCase(TestCase):
    def setUp(self):
        self.classification = Classification.objects.create(code="005", name="Fiction", description="Books that are not based on real events.")

    def test_classification_detail_view(self):
        response = self.client.get(reverse("classification_detail", args=[self.classification.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fiction")
        self.assertContains(response, "Books that are not based on real events.")

# Add, Create, Delete of Author View
class AuthorAddViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('author_form')
        self.data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
        }

    def test_author_add_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Author.objects.count(), 1)
        author = Author.objects.first()
        self.assertEqual(author.first_name, 'John')
        self.assertEqual(author.last_name, 'Doe')
        self.assertEqual(author.email, 'johndoe@example.com')

class AuthorEditViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.author = Author.objects.create(first_name='John', last_name='Doe', email='johndoe@example.com')
        self.url = reverse('author_update', kwargs={'pk': self.author.pk})
        self.data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'janedoe@example.com',
        }

    def test_author_edit_view(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 200)
        self.author.refresh_from_db()
        self.assertEqual(self.author.first_name, 'Jane')
        self.assertEqual(self.author.last_name, 'Doe')
        self.assertEqual(self.author.email, 'janedoe@example.com')

class AuthorDeleteViewTestCase(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name='Publisher A')
        self.author = Author.objects.create(first_name='John', last_name='Doe', email='johndoe@example.com')
        self.author.publisher = self.publisher
        self.author.save()
        self.url = reverse('author_delete', args=[self.author.pk])

    def test_author_delete_view_success_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_author_delete_view_not_found_status_code(self):
        response = self.client.get(reverse('author_delete', args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_author_delete_view_delete_author(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Author.objects.filter(pk=self.author.pk).exists(), False)
    



