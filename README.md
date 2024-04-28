# Написано 15 тестов. 

# 1, 2, 3

# Позитивный тест. Добавляет 2 книги в словарь books_genre. Проверяет, что при добавлении двух книг с валидным именем длина словаря books_genre равна двум, 

# а также проверка невозможности добавлени дубликатов книг. Метод добавляет одинаковые наименования, затем сверяет, что копии перезаписались 

test_add_new_book_added_two_books  

# 4, 5 

# Негативный тест. Проверяет, что книга, название которой == 0 символов ИЛИ превышает 40 символов, не добавляется в словарь books_genre. Используется параметризация
 
test_add_new_book_invalid_quantity_of_symbols  

# 6, 7

# Проверка на то, что книге можно присвоить существующий жанр

test_set_book_genre_add_book_in_genre_list

# 8

# Проверка на то, что установить жанр книги с помощью метода set_book_genre невозможно, если: книги нет в словаре books_genre ИЛИ жанр книги не входит в список genre. Использована двойная параметризация

test_set_book_genre_only_valid_items_in_genre_list  

# 9

# Проверка на то, что по названию существующей книги можно узнать ее жанр

test_get_book_genre_using_books_name

# 10

# Проверка возможности выведения книг по признаку жанра. Метод добавляет в словарь books_genre две книги одной категории и выводит длину словаря: в рез-те там появляются две позиции

test_get_books_with_specific_genre_add_two_books_of_same_genre 

# 11

#  Проверка возможности выведения жанров книг по их названиям. В метод переданы три книги разных жанров, в рез-те метод выводит длину словаря books_genre: 3 эл-та соответственно  

test_get_books_genre_add_three_books_to_genre_list  

# 12 

# Проверка возможности возврата книг определенных категорий 

test_get_books_for_children_add_two_books_only_one_valid 

# 13 

# Добавление книги в избранное 

test_add_book_in_favorites_add_book_to_favorites

# 14 

# Удаление книг из избранного 

test_delete_book_from_favorites

# 15

# Запрос наличия избранных наименований в списке favorites. Добавление книги и проверка наличия наименивания с помощью оператора in

test_list_of_favorites_books_request_favorites


