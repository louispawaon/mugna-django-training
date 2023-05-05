from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import timedelta


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Publisher")
        verbose_name_plural = _("Publishers")


class Classification(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField("exercises.Author")
    publisher = models.ForeignKey(
        "exercises.Publisher", on_delete=models.CASCADE, null=True
    )

    publication_date = models.DateField(null=True)

    def was_published_recently(self):
        date_today = timezone.now().date()
        return self.publication_date >= date_today - timedelta(day=1)

    was_published_recently.admin_order_field = "publication_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="e-mail")

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create your models here.
