# Generated by Django 3.0.5 on 2022-07-03 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20220703_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='book_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
