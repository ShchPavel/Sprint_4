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
