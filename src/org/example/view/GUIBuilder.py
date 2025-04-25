
import os # Імпортуємо модуль os для роботи з файловою системою.
import tkinter as tk # Імпортуємо основний модуль tkinter для створення GUI.
from tkinter import messagebox, ttk # Імпортуємо підмодулі messagebox та ttk (стилізовані віджети).
from PIL import Image, ImageTk # Імпортуємо класи Image та ImageTk з бібліотеки Pillow для роботи із зображеннями.
from src.org.example.view.ListBoxManager import ListboxManager # Імпортуємо клас ListboxManager для керування списками.

class GUIBuilder:
    """
    Клас для побудови графічного інтерфейсу користувача (GUI).
    Відповідає за створення та розміщення віджетів на головному вікні.
    """
    def __init__(self, root, control):
        """
        Ініціалізатор класу GUIBuilder.

        Args:
            root (tkinter.Tk): Головне вікно програми.
            control (Control): Екземпляр класу Control для взаємодії з логікою програми.
        """
        self.tk_result_img = None # Змінна для зберігання об'єкта ImageTk.PhotoImage для відображення зображення.
        self.root = root # Зберігаємо посилання на головне вікно.
        self.control = control # Зберігаємо посилання на контролер.
        self.view = None # Змінна для зберігання посилання на об'єкт GalleryView.

        self.root.title("Спортивний інвентар - ⚽🛹🏓🛼🎾") # Встановлюємо заголовок головного вікна.
        self.root.geometry("550x950") # Встановлюємо розміри головного вікна.

        self.notebook = ttk.Notebook(self.root) # Створюємо віджет Notebook для вкладок.
        self.input_tab = tk.Frame(self.notebook) # Створюємо фрейм для вкладки введення даних.
        self.obj_tab = tk.Frame(self.notebook) # Створюємо фрейм для вкладки інформації про об'єкт.
        self.notebook.add(self.input_tab, text="Ввід даних") # Додаємо вкладку введення до Notebook.
        self.notebook.add(self.obj_tab, text="Інформація") # Додаємо вкладку інформації до Notebook.
        self.notebook.pack(fill="both", expand=True) # Розміщуємо Notebook на головному вікні з розтягуванням.

        self.build_input_tab() # Викликаємо метод для побудови вмісту вкладки введення.
        self.build_output_tab() # Викликаємо метод для побудови вмісту вкладки інформації.

    def build_input_tab(self):
        """
        Метод для створення та розміщення віджетів на вкладці введення даних.
        """
        tk.Label(self.input_tab, text="Назва:").grid(row=0, column=0, sticky="w", padx=5, pady=5) # Мітка "Назва".
        self.name_entry = tk.Entry(self.input_tab, width=20) # Поле введення для назви.
        self.name_entry.grid(row=0, column=1, padx=5, pady=5) # Розміщення поля введення для назви.

        tk.Label(self.input_tab, text="Ціна (грн):").grid(row=1, column=0, sticky="w", padx=5, pady=5) # Мітка "Ціна".
        self.price_entry = tk.Entry(self.input_tab, width=10) # Поле введення для ціни.
        self.price_entry.grid(row=1, column=1, padx=5, pady=5) # Розміщення поля введення для ціни.

        tk.Label(self.input_tab, text="Вага (кг):").grid(row=2, column=0, sticky="w", padx=5, pady=5) # Мітка "Вага".
        self.weight_entry = tk.Entry(self.input_tab, width=10) # Поле введення для ваги.
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5) # Розміщення поля введення для ваги.

        tk.Label(self.input_tab, text="Діаметр (см):").grid(row=3, column=0, sticky="w", padx=5, pady=5) # Мітка "Діаметр".
        self.diameter_entry = tk.Entry(self.input_tab, width=10) # Поле введення для діаметра.
        self.diameter_entry.grid(row=3, column=1, padx=5, pady=5) # Розміщення поля введення для діаметра.

        tk.Label(self.input_tab, text="Тиск (атм):").grid(row=4, column=0, sticky="w", padx=5, pady=5) # Мітка "Тиск".
        self.pressure_entry = tk.Entry(self.input_tab, width=10) # Поле введення для тиску.
        self.pressure_entry.grid(row=4, column=1, padx=5, pady=5) # Розміщення поля введення для тиску.

        tk.Label(self.input_tab, text="Виробник:").grid(row=5, column=0, sticky="w", padx=5, pady=5) # Мітка "Виробник".
        self.manufacturer_listbox = tk.Listbox(self.input_tab, height=4, width=10, exportselection=False) # Список виробників.
        self.manufacturer_scroll = tk.Scrollbar(self.input_tab, orient=tk.VERTICAL, command=self.manufacturer_listbox.yview) # Скролбар для списку виробників.
        self.manufacturer_listbox.config(yscrollcommand=self.manufacturer_scroll.set) # Прив'язуємо скролбар до списку.
        self.manufacturer_listbox.grid(row=5, column=1, padx=5, pady=5) # Розміщення списку виробників.
        self.manufacturer_scroll.grid(row=5, column=2, sticky="ns") # Розміщення скролбара.

        self.manufacturers = ["Adidas", "Nike", "Puma"] # Початкові виробники.
        for item in self.manufacturers:
            self.manufacturer_listbox.insert(tk.END, item) # Додаємо початкових виробників до списку.

        tk.Label(self.input_tab, text="Матеріал:").grid(row=6, column=0, sticky="w", padx=5, pady=5) # Мітка "Матеріал".
        self.materials = ("Шкіра", "Гума", "Синтетика") # Варіанти матеріалів.
        self.selected_material = tk.StringVar(value=self.materials[0]) # Змінна для обраного матеріалу.
        tk.OptionMenu(self.input_tab, self.selected_material, *self.materials).grid(row=6, column=1, padx=5, pady=5) # Випадаючий список матеріалів.

        tk.Label(self.input_tab, text="Рік випуску:").grid(row=7, column=0, sticky="w", padx=5, pady=5) # Мітка "Рік випуску".
        self.years = ("2020", "2021", "2022", "2023", "2024") # Варіанти років випуску.
        self.selected_year = tk.StringVar(value=self.years[0]) # Змінна для обраного року.
        tk.OptionMenu(self.input_tab, self.selected_year, *self.years).grid(row=7, column=1, padx=5, pady=5) # Випадаючий список років.

        tk.Label(self.input_tab, text="Країна виробництва:").grid(row=8, column=0, sticky="w", padx=5, pady=5) # Мітка "Країна".
        self.countries = ("Україна", "США", "Китай", "Німеччина") # Варіанти країн.
        self.selected_country = tk.StringVar(value=self.countries[0]) # Змінна для обраної країни.
        tk.OptionMenu(self.input_tab, self.selected_country, *self.countries).grid(row=8, column=1, padx=5, pady=5) # Випадаючий список країн.

        tk.Label(self.input_tab, text="Новий виробник:").grid(row=9, column=0, sticky="w", padx=5, pady=5) # Мітка "Новий виробник".
        self.new_manufacturer_entry = tk.Entry(self.input_tab) # Поле введення для нового виробника.
        self.new_manufacturer_entry.grid(row=9, column=1, padx=5, pady=5) # Розміщення поля введення для нового виробника.

        tk.Button(self.input_tab, text="➕ Додати", command=lambda: ListboxManager.add_item(self.manufacturer_listbox, self.new_manufacturer_entry)).grid(row=10, column=1, pady=2) # Кнопка "Додати виробника".
        tk.Button(self.input_tab, text="✏️ Редагувати", command=lambda: ListboxManager.edit_item(self.manufacturer_listbox, self.new_manufacturer_entry)).grid(row=11, column=0, columnspan=2, pady=2) # Кнопка "Редагувати".
        tk.Button(self.input_tab, text="🗑️ Видалити", command=lambda: ListboxManager.delete_item(self.manufacturer_listbox)).grid(row=12, column=0, columnspan=2, pady=2) # Кнопка "Видалити".
        tk.Button(self.input_tab, text="🔃 Сортувати", command=lambda: ListboxManager.sort_items(self.manufacturer_listbox)).grid(row=11, column=1, columnspan=2, pady=2) # Кнопка "Сортувати".
        tk.Button(self.input_tab, text="↩️ Зворотній порядок", command=lambda: ListboxManager.reverse_items(self.manufacturer_listbox)).grid(row=12, column=1, columnspan=2, pady=2) # Кнопка "Зворотній порядок".

        self.image_display_label = tk.Label(self.input_tab) # Місце для відображення зображення.
        self.image_display_label.grid(row=13, column=0, columnspan=3, pady=10) # Розміщення місця для зображення.

        tk.Button(self.input_tab, text="✅ Створити об'єкт", command=self.control.create_soccer_ball).grid(row=15, column=1, pady=2) # Кнопка "Створити об'єкт".

    def build_output_tab(self):
        """
        Метод для створення та розміщення віджетів на вкладці інформації про об'єкт.
        """
        self.result_label = tk.Label(self.obj_tab, text="", font=("Arial", 12), justify=tk.CENTER) # Мітка для виведення інформації про об'єкт.
        self.result_label.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky="ew") # Розміщення мітки інформації.

        self.result_image_label = tk.Label(self.obj_tab) # Місце для відображення зображення об'єкта.
        self.result_image_label.grid(row=1, column=0, columnspan=3, padx=5, sticky="ew") # Розміщення місця для зображення об'єкта.

        ttk.Button(self.obj_tab, text="⬅️ Попередній об'єкт", command=self.control.show_previous_loaded_object).grid(row=2, column=0, padx=10, pady=5, sticky="w") # Кнопка "Попередній об'єкт".
        ttk.Button(self.obj_tab, text="➡️ Наступний об'єкт", command=self.control.show_next_loaded_object).grid(row=2, column=2, padx=10, pady=5, sticky="e") # Кнопка "Наступний об'єкт".
        ttk.Button(self.obj_tab, text="🗑️ Видалити об'єкт", command=self.control.delete_current_object, width=20).grid(row=3, column=0, columnspan=3, padx=10, sticky="ew") # Кнопка "Видалити об'єкт".

    def update_result_image(self, image_path):
        """
        Метод для оновлення зображення у віджеті відображення результатів.

        Args:
            image_path (str): Шлях до файлу зображення.
        """
        try:
            img = Image.open(image_path) # Відкриваємо зображення за шляхом.
            img = img.resize((250, 150)) # Змінюємо розмір зображення.
            self.tk_result_img = ImageTk.PhotoImage(img) # Створюємо об'єкт PhotoImage для відображення в Tkinter.
            self.result_image_label.config(image=self.tk_result_img, text="") # Встановлюємо зображення у віджеті та прибираємо текст.
            self.result_image_label.image = self.tk_result_img # Зберігаємо посилання на об'єкт PhotoImage, щоб він не був видалений збирачем сміття.
        except Exception as e: # Обробляємо можливі винятки (наприклад, файл не знайдено).
            self.result_image_label.config(image='', text=f"❌ {e}") # Виводимо повідомлення про помилку.

    def set_gallery_view(self, view):
        """
        Метод для встановлення об'єкта GalleryView та налаштування кнопок навігації.

        Args:
            view (GalleryView): Об'єкт GalleryView.
        """
        self.view = view # Зберігаємо посилання на об'єкт GalleryView.
        self.view.image_label = self.image_display_label # Передаємо віджет для відображення зображень в GalleryView.
        tk.Button(self.input_tab, text="⬅️ Попереднє", command=self.view.prev_image).grid(row=14, column=0, padx=10) # Кнопка "Попереднє" для перегортання зображень.
        tk.Button(self.input_tab, text="➡️ Наступне", command=self.view.next_image).grid(row=14, column=2, padx=10) # Кнопка "Наступне" для перегортання зображень.
