# Generated by Django 3.2.3 on 2021-06-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.DateTimeField(auto_now_add=True)),
                ('imdb', models.CharField(blank=True, max_length=200)),
                ('genre', models.CharField(choices=[('Comedy', 'Comedy'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Romantic', 'Romantic'), ('Fantastic', 'Fantastic'), ('Drama', 'Drama')], max_length=20)),
                ('actor', models.ManyToManyField(related_name='actor', to='movie.Actor')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(related_name='movie', to='movie.Movie'),
        ),
    ]