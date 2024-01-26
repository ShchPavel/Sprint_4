import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book_name',
                             ['s',  # book name len 1
                              'someBookName',  # book name len 12
                              'qweqweqweqweqweqweqweqweqweqweqweqweqweq'])  # book name len 40
    def test_add_new_book_correct_len_adding_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name',
                             ['',  # book name len 0
                              'qweqweqweqweqweqweqweqweqweqweqweqweqweqw'])  # book name len 41
    def test_add_new_book_incorrect_len_not_adding_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_name_already_in_list_not_adding_book(self, collector):
        collector.add_new_book('someBookName')
        collector.add_new_book('someBookName')
        assert len(collector.books_genre) == 1

    # set_book_genre - книга есть, жанр есть -> успешно устанавливается жанр
    def test_set_book_genre_known_book_and_genre_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('AlanWake', 'Фантастика')
        assert collector_book_without_genre.books_genre['AlanWake'] == 'Фантастика'

    # set_book_genre - книги нет, жанр есть -> жанр нечему установить
    def test_set_book_genre_unknown_book_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('randomBook', 'Фантастика')
        assert 'randomBook' not in collector_book_without_genre.books_genre

    # set_book_genre - жанра нет, книга есть -> не присваивается жанр существующей книге
    def test_set_book_genre_unknown_genre_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('AlanWake', 'НовыйЖанр')
        assert collector_book_without_genre.books_genre['AlanWake'] == ''

    # set_book_genre - жанра нет, книги нет ->
    def test_set_book_genre_unknown_book_and_genre_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('randomBook', 'НовыйЖанр')
        assert 'randomBook' not in collector_book_without_genre.books_genre

    def test_get_book_genre_known_name_getting_genre(self, collector):
        collector.add_new_book('newBook')
        collector.set_book_genre('newBook', 'Ужасы')
        assert collector.get_book_genre('newBook') == 'Ужасы'

    def test_get_book_genre_unknown_name_not_getting_genre(self, collector):
        collector.add_new_book('newBook')
        collector.set_book_genre('newBook', 'Ужасы')
        assert collector.get_book_genre('randomBook') is None
