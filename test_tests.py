import pytest


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name',
                             ['s',  # book_name len 1
                              'someBookName',  # book_name len 12
                              'qweqweqweqweqweqweqweqweqweqweqweqweqweq'])  # book_name len 40
    def test_add_new_book_correct_len_adding_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name',
                             ['',  # book_name len 0
                              'qweqweqweqweqweqweqweqweqweqweqweqweqweqw'])  # book_name len 41
    def test_add_new_book_incorrect_len_not_adding_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_name_already_in_list_not_adding_book(self, collector):
        collector.add_new_book('someBookName')
        collector.add_new_book('someBookName')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_known_book_and_genre_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('AlanWake', 'Фантастика')
        assert collector_book_without_genre.get_book_genre('AlanWake') == 'Фантастика'

    def test_set_book_genre_unknown_book_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('unknownBook', 'Фантастика')
        assert collector_book_without_genre.get_book_genre('unknownBook') is None

    def test_set_book_genre_unknown_genre_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('AlanWake', 'unknownGenre')
        assert collector_book_without_genre.get_book_genre('AlanWake') is ''

    def test_set_book_genre_unknown_book_and_genre_not_set_genre(self, collector_book_without_genre):
        collector_book_without_genre.set_book_genre('unknownBook', 'unknownGenre')
        assert collector_book_without_genre.get_book_genre('unknownBook') is None

    def test_get_book_genre_known_name_getting_genre(self, collector_book_horror_genre):
        assert collector_book_horror_genre.get_book_genre('AlanWake') == 'Ужасы'

    def test_get_book_genre_unknown_name_not_getting_genre(self, collector_book_horror_genre):
        assert collector_book_horror_genre.get_book_genre('unknownBook') is None

    def test_get_books_with_specific_genre_find_one_book_by_genre(self, collector):
        collector.add_new_book('AlanWake')
        collector.set_book_genre('AlanWake', 'Ужасы')
        collector.add_new_book('Duna')
        collector.set_book_genre('Duna', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Duna']

    def test_get_books_with_specific_genre_find_two_books_by_genre(self, collector):
        collector.add_new_book('AlanWake')
        collector.set_book_genre('AlanWake', 'Ужасы')
        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['AlanWake', 'Dracula']

    def test_get_books_genre_book_dict_returned(self, collector):
        collector.add_new_book('AlanWake')
        collector.set_book_genre('AlanWake', 'Ужасы')
        collector.add_new_book('Dracula')
        assert collector.get_books_genre() == {'AlanWake': 'Ужасы', 'Dracula': ''}

    def test_get_books_for_children_only_children_books_in_output_list(self, collector):
        collector.add_new_book('AlanWake')
        collector.set_book_genre('AlanWake', 'Ужасы')
        collector.add_new_book('LionKing')
        collector.set_book_genre('LionKing', 'Мультфильмы')
        assert collector.get_books_for_children() == ['LionKing']

    def test_add_book_in_favorites_known_book_adding(self, collector):
        collector.add_new_book('Duna')
        collector.add_book_in_favorites('Duna')
        assert collector.get_list_of_favorites_books() == ['Duna']

    def test_add_book_in_favorites_unknown_book_not_adding(self, collector):
        collector.add_book_in_favorites('unknownBook')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_adding_book_is_already_in_favourites(self, collector):
        collector.add_new_book('Duna')
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('Duna')
        assert collector.get_list_of_favorites_books() == ['Duna']

    def test_delete_book_from_favorites_remove_favourite_book_book_removed(self, collector):
        collector.add_book_in_favorites('Duna')
        collector.add_book_in_favorites('Duna')
        collector.delete_book_from_favorites('Duna')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_remove_unknown_book_favourites_not_changed(self, collector):
        collector.add_new_book('Duna')
        collector.add_book_in_favorites('Duna')
        collector.delete_book_from_favorites('unknownBook')
        assert collector.get_list_of_favorites_books() == ['Duna']

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Duna')
        collector.add_book_in_favorites('Duna')
        assert collector.get_list_of_favorites_books() == ['Duna']
