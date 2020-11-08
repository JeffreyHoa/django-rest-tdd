import pytest
from movies.models import Movie

@pytest.fixture(scope='function')
def add_movie():
    '''
      返回的 _add_movie才是作为了引用地儿的参数
    '''
    print("[my debug] out: add_movie()")
    def _add_movie(title, genre, year):
        print("[my debug] in: _add_movie()")
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie
    return _add_movie
