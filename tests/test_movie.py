import pytest
from viewing_party.movie import Movie

def test_initialize_movie():
    # Arrange
    movie = Movie("The Princess Bride", "comedy", 5)
    # Act

    # Assert
    assert movie.name == "The Princess Bride"
    assert movie.genre == "comedy"
    assert movie.rating == 5
    assert movie.rating >= 1 and movie.rating <= 5