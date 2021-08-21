from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from movie.models import Actor, Movie, Comment
from movie.serializers import ActorSerializer, MovieSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['imdb', '-imdb']
    search_fields = ['name', 'genre']

    @action(detail=True, methods=["POST"], url_path='add-actor')
    def AddActor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = Actor.objects.get_or_create(name=request.data['name'], birthdate=request.data['birthdate'],
                                            gender=request.data['gender'])[0]
        movie.actor.add(actor)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["POST"], url_path='remove-actor')
    def RemoveActor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = movie.actor.last()
        movie.actor.remove(actor)
        movie.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["GET"], url_path='actors')
    def Actors(self, request, *args, **kwargs):
        movie = self.get_object()
        actor = movie.actor.all()
        serializer = ActorSerializer(actor, many=True)
        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         return Comment.objects.filter(user_id=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.validated_data['user_id'] = self.request.user
#         serializer.save()


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(user_id=request.user.id)
        n = 0
        for comment in comments:
            comment.count = n
            n += 1
            comment.save()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        comment = Comment.objects.filter(count=pk)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
