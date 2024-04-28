import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_added_two_books(self):

        book = BooksCollector()
        book.add_new_book('Книга Робинзон')
        book.add_new_book('Книга Робинзон')
        book.add_new_book('Детское')
        book.add_new_book('Детское')

        assert len(book.get_books_genre()) == 2

    @pytest.mark.parametrize('test_input', ['', 'MoreThanFourtySybmolsMoreThanFourtySybmols'])

    def test_add_new_book_invalid_quantity_of_symbols(self, test_input):

        book = BooksCollector()

        book.add_new_book(test_input)

        assert book.get_books_genre() == {}

    @pytest.mark.parametrize('test_input', ['Драма', 'Приключения'])

    def test_set_book_genre_add_invalid_genres(self, test_input):

        book = BooksCollector()

        book.add_new_book(test_input)

        assert book.set_book_genre('Тарзан', test_input) == None

    def test_set_book_genre_add_book_in_genre_list(self):
        book = BooksCollector()
        book.add_new_book('Книга тестов')
        book.set_book_genre('Книга тестов', 'Ужасы')

        assert book.get_book_genre('Книга тестов') == 'Ужасы'


    @pytest.mark.parametrize('no_book_in_genre, invalid_genre',
        [
            ['Несуществующая_книга_1', 'Несуществующая_книга_2'],
            ['Драма', 'Приключения']
        ]
    )
    def test_set_book_genre_only_valid_items_in_genre_list(self, no_book_in_genre, invalid_genre):

        book = BooksCollector()

        book.set_book_genre(no_book_in_genre, 'Ужасы')

        book.add_new_book(invalid_genre)

        assert book.set_book_genre(no_book_in_genre, 'Ужасы') or book.add_new_book(invalid_genre) == None


    def test_get_book_genre_using_books_name(self):

        book = BooksCollector()
        book.add_new_book('Сценарии')
        book.set_book_genre('Сценарии', 'Детективы')

        assert book.get_book_genre('Сценарии') == 'Детективы'

    def test_get_books_with_specific_genre_add_two_books_of_same_genre(self):

        book = BooksCollector()
        book.add_new_book('Царство QA')
        book.add_new_book('Чем заняться на выходных')
        book.set_book_genre('Царство QA', 'Мультфильмы')
        book.set_book_genre('Чем заняться на выходных', 'Мультфильмы')

        assert len(book.get_books_with_specific_genre('Мультфильмы')) == 2

    def test_get_books_genre_add_three_books_to_genre_list(self):

        book = BooksCollector()
        book.add_new_book('Тестирование и сон')
        book.add_new_book('Автоматизация')
        book.add_new_book('Pytest')

        book.set_book_genre('Тестирование и сон', 'Фантастика')
        book.set_book_genre('Автоматизация', 'Ужасы')
        book.set_book_genre('Pytest', 'Детективы')

        assert len(book.get_books_genre()) == 3

    def test_get_books_for_children_add_two_books_only_one_valid(self):

        book = BooksCollector()
        book.add_new_book('Ручное тестирование')
        book.add_new_book('Автотестирование')

        book.set_book_genre('Ручное тестирование', 'Мультфильмы')
        book.set_book_genre('Автотестирование', 'Детективы')

        assert len(book.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_book_to_favorites(self):

        book = BooksCollector()
        book.add_new_book('Любимая книга')
        book.add_book_in_favorites('Любимая книга')
        book.get_list_of_favorites_books()

        assert 'Любимая книга' in book.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):

        book = BooksCollector()
        book.add_new_book('Book to delete')
        book.add_book_in_favorites('Book to delete')
        book.delete_book_from_favorites('Book to delete')

        assert 'Book to delete' not in book.get_list_of_favorites_books()

    def test_list_of_favorites_books_request_favorites(self):

        book = BooksCollector()
        book.add_new_book('Fav_book')
        book.add_book_in_favorites('Fav_book')
        book.get_list_of_favorites_books()

        assert 'Fav_book' in book.get_list_of_favorites_books()
