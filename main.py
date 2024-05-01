class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites




book = BooksCollector()
book.add_new_book('Fav_book_1')

#book.set_book_genre('Fav_book_1', 'Фантастика')

book.add_book_in_favorites('Fav_book_1')

print(book.get_list_of_favorites_books())

print(book.favorites)

print('Fav_book_1' in book.favorites)

#print(book.get_books_genre())




#print(len(book.get_books_genre()))
#print(book.__dict__.values())





   # print(True)


#if 'Детективы' in book.books_genre.values():  # неправильный вариант - обращение напрямую к атрибуту
#    print(True)
#else:
#    print(False)

#print(book.get_books_genre())

#print(list(book.books_genre.values()))


#if 'Детективы' in book.get_books_genre().values():  # правильный вариант - обращение через метод, используя методы keys and values(тоже со скобками естественно)
#    print(True)
#else:
#    print(False)

