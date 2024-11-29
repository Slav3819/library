import uuid
class Book:
    def __init__(self, title, author, year):
        self.id = str(uuid.uuid4())[:8]  # Уникальный ID
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"  # Статус по умолчанию

    def display_info(self):
        print(f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}")

class Library:
    def __init__(self):
        self.books = []  # Список книг

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Книга '{title}' добавлена.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f"Книга с ID {book_id} удалена.")
                return
        print("Книга не найдена.")

    def search_book(self, keyword):
        found_books = [book for book in self.books if
                       keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                book.display_info()
        else:
            print("Книги не найдены.")

    def display_books(self):
        if self.books:
            for book in self.books:
                book.display_info()
        else:
            print("Библиотека пуста.")

    def change_status(self, book_id, new_status):
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print(f"Статус книги '{book.title}' изменен на '{new_status}'.")
                return
        print("Книга не найдена.")


# Основное меню программы
def main():
    library = Library()
    while True:
        print(
            "\n1. Добавить книгу\n2. Удалить книгу\n3. Найти книгу\n4. Показать все книги\n5. Изменить статус книги\n6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)
        elif choice == '3':
            keyword = input("Введите название или автора книги для поиска: ")
            library.search_book(keyword)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = input("Введите ID книги: ")
            new_status = input("Введите новый статус (1 - 'в наличии' или 2 - 'выдана'): ")
            if new_status == '1':
                library.change_status(book_id, 'в наличии')
            elif new_status == '2':
                library.change_status(book_id, 'выдана')
            else:
                print("Неверный ввод статус не изменен")

        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == '__main__':
    main()




