from tkinter import * # Імпортуємо всі класи та константи з бібліотеки tkinter.
# tkinter використовується для створення графічного інтерфейсу користувача.
from PIL import Image, ImageTk # Імпортуємо класи Image та ImageTk з бібліотеки Pillow (PIL Fork).
# Pillow використовується для роботи з зображеннями (відкриття, редагування, збереження).
# ImageTk використовується для відображення зображень Pillow у віджетах tkinter.


class GalleryView:
    """
    Клас, що відповідає за відображення галереї зображень футбольних м'ячів.
    """
    def __init__(self, parent_frame):
        """
        Конструктор класу GalleryView.

        Args:
            parent_frame (tkinter.Frame): Батьківський фрейм (контейнер), в якому буде розміщено галерею.
        """
        # Галерея зображень
        self.image_paths_soccer_ball = ["../../../resource/img/ball/adidas.png", # Список шляхів до зображень футбольних м'ячів.
                                        "../../../resource/img/ball/puma.png",
                                        "../../../resource/img/ball/ball3.png"]
        self.current_index = 0 # Індекс поточного зображення, що відображається в галереї (початкове значення - 0).
        self.image_label = Label(parent_frame) # Створюємо віджет Label (мітку) для відображення зображення
        # у переданому батьківському фреймі (parent_frame).
        # Атрибут self.image_label зберігає посилання на цей віджет.
        self.image_label.grid(row=15, column=0, columnspan=2, pady=10) # Розміщуємо віджет image_label у сітці
        # батьківського фрейма.
        # row=15: розміщення у 16-му рядку.
        # column=0: розміщення у першому стовпці.
        # columnspan=2: розтягування на два стовпці.
        # pady=10: вертикальний відступ у 10 пікселів.

    def show_image_ball(self):
        """
        Метод для відображення поточного зображення футбольного м'яча з галереї.
        """
        try:
            img = Image.open(self.image_paths_soccer_ball[self.current_index]) # Відкриваємо зображення за шляхом,
            # що відповідає поточному індексу.
            # self.image_paths_soccer_ball - список шляхів до зображень.
            # self.current_index - індекс поточного зображення.
            img = img.resize((250, 150)) # Змінюємо розмір зображення до 250x150 пікселів.
            self.tk_img = ImageTk.PhotoImage(img) # Створюємо об'єкт PhotoImage з зображення Pillow для відображення в tkinter.
            self.image_label.config(image=self.tk_img) # Оновлюємо віджет image_label, встановлюючи йому нове зображення.
        except Exception as e: # Обробляємо можливі помилки при відкритті або обробці зображення.
            self.image_label.config(text=f"Помилка завантаження зображення\n{e}") # Виводимо повідомлення про помилку у віджеті label.

    def next_image(self):
        """
        Метод для переходу до наступного зображення в галереї.
        """
        self.current_index = (self.current_index + 1) % len(self.image_paths_soccer_ball) # Збільшуємо індекс на 1.
        # Оператор % (modulo) забезпечує циклічний перехід
        # (після останнього зображення знову показується перше).
        self.show_image_ball() # Викликаємо метод для відображення нового поточного зображення.

    def prev_image(self):
        """
        Метод для переходу до попереднього зображення в галереї.
        """
        self.current_index = (self.current_index - 1) % len(self.image_paths_soccer_ball) # Зменшуємо індекс на 1.
        # Знову ж таки, % забезпечує циклічність
        # (перед першим зображенням показується останнє).
        self.show_image_ball() # Викликаємо метод для відображення нового поточного зображення.

    def clear_image(self):
        """
        Метод для очищення відображеного зображення в галереї.
        """
        self.image_label.config(text="") # Очищаємо текст віджета image_label (фактично прибираємо зображення).
        self.current_index = 0 # Скидаємо індекс на початкове значення.
        self.show_image_ball() # Відображаємо початкове зображення.

    def get_current_image_path(self):
        """
        Метод для отримання шляху до поточного відображеного зображення.

        Returns:
            str: Шлях до файлу поточного зображення.
        """
        return self.image_paths_soccer_ball[self.current_index] # Повертаємо шлях зі списку за поточним індексом.