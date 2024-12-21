from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        genre = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert genre == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert sorted(collector.get_books_with_specific_genre('Комедии')) == sorted(
            ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби'])

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Тупой и еще тупее')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        collector.set_book_genre('Тупой и еще тупее', 'Комедии')
        result = collector.get_books_genre()
        book = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Фантастика',
            'Тупой и еще тупее': 'Комедии'
        }
        assert book == result

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Лунтик')
        collector.add_book_in_favorites('Лунтик')
        collector.delete_book_from_favorites('Лунтик')
        assert 'Лунтик' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Лунтик')
        collector.add_new_book('Маша и Медведь')
        collector.add_book_in_favorites('Лунтик')
        collector.add_book_in_favorites('Маша и Медведь')
        favorite_books = collector.get_list_of_favorites_books()
        expected_books = {'Лунтик',
                          'Маша и Медведь'}
        assert expected_books == set(favorite_books), "Список избранных книг не соответствует ожидаемому."

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Лунтик')
        collector.set_book_genre('Лунтик', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        expected_books = ['Лунтик']
        assert sorted(expected_books) == sorted(children_books), "Список книг для детей не соответствует ожидаемому."

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        name = 'Лунтик'
        genre = 'Мультфильмы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites
