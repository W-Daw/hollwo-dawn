# Generated by Django 3.0.3 on 2020-08-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keshe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='b_isbn',
            field=models.CharField(max_length=40),
        ),
    ]
