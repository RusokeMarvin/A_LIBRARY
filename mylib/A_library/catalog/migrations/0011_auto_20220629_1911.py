# Generated by Django 3.0.5 on 2022-06-29 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_student_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='fine_ammount',
            new_name='fine_amount',
        ),
    ]
