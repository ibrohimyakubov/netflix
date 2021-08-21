from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Actor(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    name = models.CharField(max_length=200, blank=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER)

    def __str__(self):
        return self.name

    verbose_name = 'actor'


class Movie(models.Model):
    GENRES = [
        ('Comedy', 'Comedy'),
        ('Thriller', 'Thriller'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Fantastic', 'Fantastic'),
        ('Drama', 'Drama'),
    ]
    name = models.CharField(max_length=200, blank=False)
    year = models.DateField()
    imdb = models.SmallIntegerField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=GENRES)
    actor = models.ManyToManyField(Actor, related_name='actor', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    text = models.TextField()
    count = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_id} - {self.user_id}"
