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
                             ['s',                                                          # book_name len 1
                              'someBookName',                                               # book_name len 12
                              'qweqweqweqweqweqweqweqweqweqweqweqweqweq'])                  # book_name len 40
    def test_add_new_book_correct_len_adding_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name',
                             ['',                                                           # book_name len 0
                              'qweqweqweqweqweqweqweqweqweqweqweqweqweqw'])                 # book_name len 41
    def test_add_new_book_incorrect_len_not_adding_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_name_already_in_list_not_adding_book(self, collector):
        collector.add_new_book('someBookName')
        collector.add_new_book('someBookName')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_known_book_and_genre_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('AlanWake', 'Фантастика')
        assert collector_book_without_genre.books_genre['AlanWake'] == 'Фантастика'

    def test_set_book_genre_unknown_book_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('unknownBook', 'Фантастика')
        assert 'randomBook' not in collector_book_without_genre.books_genre

    def test_set_book_genre_unknown_genre_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('AlanWake', 'unknownGenre')
        assert collector_book_without_genre.books_genre['AlanWake'] == ''

    def test_set_book_genre_unknown_book_and_genre_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('unknownBook', 'unknownGenre')
        assert 'randomBook' not in collector_book_without_genre.books_genre

    def test_get_book_genre_known_name_getting_genre(self, collector_book_horror_genre):
        expected_genre = collector_book_horror_genre.get_book_genre('AlanWake')
        assert expected_genre == 'Ужасы'

    def test_get_book_genre_unknown_name_not_getting_genre(self, collector_book_horror_genre):
        expected_genre = collector_book_horror_genre.get_book_genre('unknownBook')
        assert expected_genre is None

    def test_get_books_with_specific_genre_find_books_by_genre(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        filtered_film_list = collector.get_books_with_specific_genre('Фантастика')
        assert len(filtered_film_list) == 3 and ('1984' and 'LordOfTheRings' and 'Duna') in filtered_film_list

    def test_get_books_genre_input_list_equals_to_result(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        assert collector.get_books_genre() == list_of_some_books

    def test_get_books_for_children_only_children_books_in_output_list(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        assert (('LordOfTheRings' and 'Duna' and '1984' and 'TheLionKing'
                 and 'Winnie-the-Pooh' and 'Great Falls' and 'Kind of a Big Deal') in collector.get_books_for_children()
                and len(collector.get_books_for_children()) == 7)

    def test_add_book_in_favorites_is_known_book_adding_to_favourites(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('1984')
        assert 'Duna' and '1984' in collector.favorites

    def test_add_book_in_favorites_is_unknown_book_not_adding_to_favourites(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        collector.add_book_in_favorites('WalkingDead')
        collector.add_book_in_favorites('HarryPotter')
        assert len(collector.favorites) == 0

    def test_add_book_in_favorites_adding_book_is_already_in_favourites(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('Duna')
        assert len(collector.favorites) == 1 and 'Duna' in collector.favorites

    def test_delete_book_from_favorites_remove_favourite_book_book_removed(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert len(collector.favorites) == 1 and 'Duna' in collector.favorites

    def test_delete_book_from_favorites_remove_unknown_book_favourites_not_changed(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('unknownBook')
        assert len(collector.favorites) == 2 and ('Duna' and '1984') in collector.favorites

    def test_get_list_of_favorites_books(self, collector, list_of_some_books):
        collector.books_genre = list_of_some_books
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('Duna')
        collector.add_book_in_favorites('Dracula')
        assert (len(collector.get_list_of_favorites_books()) == 2 and
                ('1984' and 'Dracula') in collector.get_list_of_favorites_books())