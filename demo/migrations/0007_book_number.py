# Generated by Django 3.1.1 on 2020-09-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_author_booknumber_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.booknumber'),
        ),
    ]