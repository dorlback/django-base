# Generated by Django 5.0.6 on 2024-06-05 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0002_alter_book_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book",
                to="book_app.author",
            ),
        ),
    ]
