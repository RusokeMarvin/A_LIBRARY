# Generated by Django 4.0.5 on 2022-07-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Password',
            field=models.CharField(max_length=50),
        ),
    ]