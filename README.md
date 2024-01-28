# Список реализованных тестов с пояснениями
### test_add_new_book_add_two_books - проверка длины списка books_genre при добавлении книг 
### test_add_new_book_correct_len_adding_book - позитивные проверки возможности добавления книги в зависимости от длины названия книги
### test_add_new_book_incorrect_len_not_adding_book - негативные проверки возможности добавления книги в зависимости от длины названия книги
### test_add_new_book_name_already_in_list_not_adding_book - проверка возможности добавить книгу с одинаковым именем несколько раз
### test_set_book_genre_known_book_and_genre_set_genre - проверка возможности добавления к книге из books_genre жанра из genre 
### test_set_book_genre_unknown_book_not_set_genre - проверка возможности добавления к книге которой нет в books_genre жанра из genre
### test_set_book_genre_unknown_genre_not_set_genre - проверка возможности добавления к книге из books_genre жанра, которого нет в genre
### test_set_book_genre_unknown_book_and_genre_not_set_genre - проверка возможности добавления к книге, которой нет в books_genre, жанра, которого нет в genre
### test_get_book_genre_known_name_getting_genre - проверка получения жанра для книги из списка books_genre с установленном жанром
### test_get_book_genre_unknown_name_not_getting_genre - проверка получения жанра для книги, которой нет в списке books_genre
### test_get_books_with_specific_genre_find_book_by_genre - проверка получения списка с книгой по жанру
### test_get_books_with_specific_genre_find_two_books_by_genre -  проверка получения списка книг по их жанру
### test_get_books_genre_book_dict_returned - проверка получения списка всех книг с их жанрами
### test_get_books_for_children_only_children_books_in_output_list - проверка получения списка книг только для детей, т.е. не ужасы и не детективы
### test_add_book_in_favorites_known_book_adding - проверка добавления книг из списка books_genre в список favorites
### test_add_book_in_favorites_unknown_book_not_adding - проверка добавления книг, которых нет в списке books_genre, в список favorites
### test_add_book_in_favorites_adding_book_is_already_in_favourites - проверка добавление одной и той же книги несколько раз из списка books_genre в список favorites
### test_delete_book_from_favorites_remove_favourite_book_book_removed - проверка удаления книги, присутствующей в списке favorites, из этого осписка
### test_delete_book_from_favorites_remove_unknown_book_favourites_not_changed - проверка удаления книги, которой нет в списке favourites, из него
### test_get_list_of_favorites_books - проверка получения списка книг, которые находятся в списке favourites