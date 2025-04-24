from tkinter import Tk # Імпортуємо клас Tk з бібліотеки tkinter.
# Tk є основним віконним контейнером для GUI-додатків tkinter.

from src.org.example.view.GUIBuilder import GUIBuilder # Імпортуємо клас GUIBuilder з вказаного модуля.
# GUIBuilder відповідає за побудову графічного інтерфейсу програми.
from src.org.example.view.GalleryView import GalleryView # Імпортуємо клас GalleryView з вказаного модуля.
# GalleryView відповідає за відображення галереї зображень.


class App:
    def __init__(self, root):
        """
        Конструктор класу App.

        Args:
            root (Tk): Основний віконний контейнер tkinter, в якому буде розміщено GUI.
        """
        self.gui = GUIBuilder(root) # Створюємо екземпляр класу GUIBuilder, передаючи йому основне вікно root.
        # Атрибут self.gui зберігає посилання на об'єкт GUIBuilder,
        # через який ми будемо взаємодіяти з елементами інтерфейсу.
        self.view = GalleryView(self.gui.input_tab) # Створюємо екземпляр класу GalleryView,
        # передаючи йому вкладку для вводу даних (self.gui.input_tab)
        # як батьківський контейнер.
        # Атрибут self.view зберігає посилання на об'єкт GalleryView.
        # self.gui.input_tab - це атрибут об'єкта GUIBuilder,
        # який є фреймом (контейнером) у вкладці "Ввід даних".
        self.gui.set_gallery_view(self.view) # Викликаємо метод set_gallery_view об'єкта GUIBuilder,
        # передаючи йому об'єкт GalleryView (self.view).
        # Цей метод, ймовірно, налаштовує зв'язок між GUI та галереєю.
        self.view.show_image_ball() # Викликаємо метод show_image_ball об'єкта GalleryView (self.view),
        # який відповідає за відображення початкового зображення в галереї.


if __name__ == "__main__":
    root = Tk() # Створюємо основне вікно програми, екземпляр класу Tk.
    app = App(root) # Створюємо екземпляр класу App, передаючи йому основне вікно root.
    root.mainloop() # Запускаємо головний цикл обробки подій tkinter.
    # Цей метод утримує вікно відкритим та відповідає на дії користувача (натискання кнопок, введення тексту тощо).