# Generated by Django 4.2.5 on 2023-09-29 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_favoritemovie_reviewmovie_movies_genre_movies_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(null=True, upload_to='movies/'),
        ),
    ]
