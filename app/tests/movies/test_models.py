import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="xxx", genre="comedy", year="2020")
    movie.save()
    assert movie.title == "xxx"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title
