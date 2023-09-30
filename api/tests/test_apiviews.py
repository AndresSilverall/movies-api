from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class TestApiViews(TestCase):
    def setUp(self) -> None:

        self.client = APIClient()
        self.movies = self.client.get('/api/movies/', format="json")
        self.movie_detail = self.client.get('/api/movie/detail/3', format="json")
        self.data = {

            "title": "Spider-Man: Web of Shadows",
            "description": "Spider-Man faces a new threat when a deadly symbiote invasion takes over New York City. He must make tough choices to save the city and himself.",
            "director": "Sam Raimi",
            "genre": "Action",
            "writer": "Stan Lee",
            "year": 2008
        }

        self.add_movie = self.client.post('/api/add/movie/', data=self.data, content_type="application/json")


    def test_api_view_get_all_movies_status_code_success(self):
        self.assertEquals(self.movies.status_code, status.HTTP_200_OK, 
                         msg="Should return a 200 status code.")


    def test_api_view_get_all_movies_status_code_not_404(self):
        self.assertNotEquals(self.movies.status_code, status.HTTP_404_NOT_FOUND, 
                            msg="Should not return a 404 status code.")

    
    def test_api_view_get_movie_detail_success(self):
        self.assertEquals(self.movie_detail.status_code, status.HTTP_200_OK, 
                         msg="Should return a 200 satus code.")

    
    def test_api_view_add_movie_post(self):
        self.assertEquals(self.add_movie.status_code, status.HTTP_201_CREATED,
                         msg="Should return a 201 status code when the user add a new movie.")
