from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class TestApiViews(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.movies = self.client.get('/api/movies/', format="json")
        self.movie_detail = self.client.get('api/movie/detail/98', format="json")


    def test_api_view_status_code_success(self):
        self.assertEquals(self.movies.status_code, status.HTTP_200_OK)


    def test_api_view_status_code_error(self):
        self.assertNotEquals(self.movies.status_code, status.HTTP_404_NOT_FOUND)