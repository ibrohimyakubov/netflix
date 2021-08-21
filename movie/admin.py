from django.contrib import admin
from movie.models import Movie, Actor, Comment


admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Comment)
