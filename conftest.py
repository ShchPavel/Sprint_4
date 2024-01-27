import pytest
import main


@pytest.fixture()
def collector():
    return main.BooksCollector()


@pytest.fixture()
def collector_book_without_genre(collector):
    collector.add_new_book('AlanWake')
    return collector


@pytest.fixture()
def collector_book_horror_genre(collector_book_without_genre):
    collector_book_without_genre.set_book_genre('AlanWake', 'Ужасы')
    return collector_book_without_genre


@pytest.fixture()
def list_of_some_books():
    film_list = {
        'LordOfTheRings': 'Фантастика',
        'Duna': 'Фантастика',
        '1984': 'Фантастика',
        'AlanWake': 'Ужасы',
        'Dracula': 'Ужасы',
        'The Memoirs of Sherlock Holmes': 'Детективы',
        'The Da Vinci Code': 'Детективы',
        'TheLionKing': 'Мультфильмы',
        'Winnie-the-Pooh': 'Мультфильмы',
        'Great Falls': 'Комедии',
        'Kind of a Big Deal': 'Комедии'
    }
    return film_list
