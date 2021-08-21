from rest_framework import serializers
from movie.models import Movie, Actor, Comment, User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'birthdate', 'gender']

    def validate_birthdate(self, value):
        if value.year < 1950:
            raise ValidationError(detail='birthdate mus be big to 01.01.1950')
        return value


class MovieSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['movie_id', 'user_id', 'text', 'count']
