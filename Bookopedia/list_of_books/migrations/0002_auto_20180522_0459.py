# Generated by Django 2.0.5 on 2018-05-22 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image_file', models.ImageField(default='', upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type_of_book', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='list_of_books.Type')),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='type_of_book',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
