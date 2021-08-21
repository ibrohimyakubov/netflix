from django.test import TestCase, Client
from movie.models import Movie


class TestMovieVeiwSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test 1', genre='Comedy', year='1990-06-13')
        self.client = Client()

    def test_get_all_movie(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Test 1')
        self.assertEquals(data[0]['genre'], 'Comedy')
        self.assertEquals(data[0]['year'], '1990-06-13')


class TestSearchMoviesView(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test 1', genre='Comedy', year='1990-06-13', imdb=3)
        self.movie = Movie.objects.create(name='Test 2', genre='Horror', year='2001-06-13', imdb=9)
        self.client = Client()

    def test_search(self):
        response = self.client.get('/movies/?search=Test 1')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], 'Test 1')

    def ordering_imdb(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['name'], 'Test 2')

