import pytest
from viewing_party.person import Person

def test_create_person():
    # Arrange / Act
    kendall = Person("Kendall", ["Nancy"], [], [])

    # Assert
    assert isinstance(kendall, Person)

def test_person_name_is_set_correctly():
    # Arrange / Act
    nancy = Person("Nancy", ["Kendall"], [], [])
    danica = Person("Danica", ["Ping"], [], [])

    # Assert
    assert nancy.name == "Nancy"
    assert danica.name == "Danica"

def test_person_friends_list_is_set_correctly():
    # Arrange / Act
    ana = Person("Ana", ["Ariel"], [], [])

    # Assert
    assert ana.friends == ["Ariel"]

def test_friend_added_to_person():
    # Arrange
    laura = Person("Laura", ["Sage"], [], [])

    # Act
    laura.add_friend("Elizabeth")

    # Assert
    assert laura.friends == ["Sage", "Elizabeth"]

def test_no_duplicate_friends_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], [], [])

    # Act
    moyo.add_friend("Sarah")

    # Assert
    assert moyo.friends == ["Sarah"]

def test_new_movie_added_to_watchlist():
    # Arrange
    danica = Person("Danica", ["Sage"], ["The Princess Bride"],[])

    # Act
    danica.add_to_watchlist("What We Do In the Shadows")

    # Assert
    assert danica.watchlist == ["The Princess Bride", "What We Do In the Shadows"]
    assert len(danica.watchlist) == 2

def test_no_duplicate_added_to_watchlist():
    # Arrange
    danica = Person("Danica", ["Sage"], ["The Princess Bride"],[])

    # Act
    danica.add_to_watchlist("The Princess Bride")

    # Assert
    assert danica.watchlist == ["The Princess Bride"]
    assert len(danica.watchlist) == 1

def test_add_movie_from_watchlist_to_watched():
    # Arrange
    sage = Person("Sage", ["Danica"], ["What We Do in the Shadows"], ["The Princess Bride"])

    # Act 
    sage.watch_movie("What We Do in the Shadows")

    # Assert
    assert sage.watchlist == []
    assert sage.watched == ["The Princess Bride", "What We Do in the Shadows"]

def test_add_new_movie_not_from_watchlist():
    # Arrange
    sage = Person("Sage", ["Danica"], ["What We Do in the Shadows"], ["The Princess Bride"])

    # Act 
    sage.watch_movie("Cars")

    # Assert
    assert sage.watchlist == ["What We Do in the Shadows"]
    assert sage.watched == ["The Princess Bride", "Cars"]


def test_no_duplicates_in_watched():
    # Arrange
    sage = Person("Sage", ["Danica"], ["What We Do in the Shadows"], ["The Princess Bride"])

    # Act 
    sage.watch_movie("The Princess Bride")

    # Assert
    assert sage.watchlist == ["What We Do in the Shadows"]
    assert sage.watched == ["The Princess Bride"]  