# Generated by Django 4.2 on 2023-05-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exercises", "0004_alter_author_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.EmailField(max_length=254, null=True, verbose_name="e-mail"),
        ),
    ]
