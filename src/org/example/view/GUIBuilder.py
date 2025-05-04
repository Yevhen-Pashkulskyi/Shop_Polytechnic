import os # Імпортує модуль os для роботи з операційною системою, наприклад, для створення директорій та перевірки існування файлів.
import tkinter as tk # Імпортує модуль tkinter для створення графічного інтерфейсу користувача (GUI).  Зазвичай імпортується як tk.
from tkinter import messagebox, ttk # Імпортує підмодулі messagebox та ttk з tkinter.
#   - messagebox: для відображення вікон повідомлень (помилки, попередження, запити).
#   - ttk: для використання стилізованих віджетів (кнопки, мітки, тощо).
from PIL import Image, ImageTk # Імпортує класи Image та ImageTk з модуля PIL (Python Imaging Library) або Pillow.
#   - Image: для відкриття та маніпулювання зображеннями.
#   - ImageTk: для відображення зображень у tkinter.
from src.org.example.view.ListBoxManager import ListboxManager # Імпортує клас ListboxManager з модуля ListboxManager.py.
#   Цей клас, ймовірно, містить методи для управління елементами віджету Listbox.

class GUIBuilder:
    """
    Клас GUIBuilder відповідає за побудову графічного інтерфейсу користувача (GUI) для програми.
    Він використовує бібліотеку tkinter для створення вікон, кнопок, полів вводу та інших елементів керування.
    """
    def __init__(self, root, control):
        """
        Ініціалізує об'єкт GUIBuilder.

        Args:
            root (tk.Tk): Кореневий об'єкт Tkinter, який представляє головне вікно програми.
            control (Control): Об'єкт класу Control, який відповідає за логіку програми та обробку подій.
        """
        self.tk_result_img = None # Змінна для зберігання об'єкта PhotoImage, який відображає результатне зображення.  Початково None.
        self.root = root # Зберігає посилання на кореневий об'єкт Tkinter.
        self.control = control # Зберігає посилання на об'єкт Control.
        self.view = None # Змінна для зберігання посилання на об'єкт GalleryView.  Початково None.

        self.root.title("Спортивний інвентар - ⚽🛹🏓🛼🎾") # Встановлює заголовок головного вікна.
        self.root.geometry("550x950") # Встановлює розміри головного вікна (ширина x висота).

        self.notebook = ttk.Notebook(self.root) # Створює об'єкт Notebook, який дозволяє розміщувати декілька вкладок в одному вікні.
        self.input_tab = tk.Frame(self.notebook) # Створює фрейм (контейнер) для вкладки "Ввід даних".
        self.obj_tab = tk.Frame(self.notebook) # Створює фрейм для вкладки "Інформація".
        self.notebook.add(self.input_tab, text="Ввід даних") # Додає вкладку "Ввід даних" у Notebook.
        self.notebook.add(self.obj_tab, text="Інформація") # Додає вкладку "Інформація" у Notebook.
        self.notebook.pack(fill="both", expand=True) # Розміщує Notebook у головному вікні, заповнюючи весь доступний простір.

        self.build_input_tab() # Викликає метод для побудови вмісту вкладки "Ввід даних".
        self.build_output_tab() # Викликає метод для побудови вмісту вкладки "Інформація".

    def build_input_tab(self):
        """
        Створює та розміщує віджети на вкладці "Ввід даних".
        Віджети включають мітки, поля вводу, списки, кнопки для введення даних про об'єкт (наприклад, футбольний м'яч).
        """
        tk.Label(self.input_tab, text="Назва:").grid(row=0, column=0, sticky="w", padx=5, pady=5) # Створює мітку "Назва:" та розміщує її у вказаній комірці таблиці.  sticky="w" вирівнює текст по лівому краю.
        self.name_entry = tk.Entry(self.input_tab, width=20) # Створює поле вводу для назви об'єкта.
        self.name_entry.grid(row=0, column=1, padx=5, pady=5) # Розміщує поле вводу у вказаній комірці таблиці.

        tk.Label(self.input_tab, text="Ціна (грн):").grid(row=1, column=0, sticky="w", padx=5, pady=5) # Мітка для ціни.
        self.price_entry = tk.Entry(self.input_tab, width=10) # Поле вводу для ціни.
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Вага (кг):").grid(row=2, column=0, sticky="w", padx=5, pady=5) # Мітка для ваги.
        self.weight_entry = tk.Entry(self.input_tab, width=10) # Поле вводу для ваги.
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Діаметр (см):").grid(row=3, column=0, sticky="w", padx=5, pady=5) # Мітка для діаметру.
        self.diameter_entry = tk.Entry(self.input_tab, width=10) # Поле вводу для діаметру.
        self.diameter_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Тиск (атм):").grid(row=4, column=0, sticky="w", padx=5, pady=5) # Мітка для тиску.
        self.pressure_entry = tk.Entry(self.input_tab, width=10) # Поле вводу для тиску.
        self.pressure_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Виробник:").grid(row=5, column=0, sticky="w", padx=5, pady=5) # Мітка для виробника.
        self.manufacturer_listbox = tk.Listbox(self.input_tab, height=4, width=10, exportselection=False) # Створює список для вибору виробника. exportselection=False дозволяє виділяти елементи списку, не забираючи фокус з інших віджетів.
        self.manufacturer_scroll = tk.Scrollbar(self.input_tab, orient=tk.VERTICAL, command=self.manufacturer_listbox.yview) # Створює смугу прокрутки для списку.
        self.manufacturer_listbox.config(yscrollcommand=self.manufacturer_scroll.set) # Зв'язує смугу прокрутки зі списком.
        self.manufacturer_listbox.grid(row=5, column=1, padx=5, pady=5) # Розміщує список.
        self.manufacturer_scroll.grid(row=5, column=2, sticky="ns") # Розміщує смугу прокрутки. sticky="ns" розтягує смугу прокрутки по вертикалі.

        self.manufacturers = ["Adidas", "Nike", "Puma"] # Список виробників.
        for item in self.manufacturers:
            self.manufacturer_listbox.insert(tk.END, item) # Додає виробників у список.

        tk.Label(self.input_tab, text="Матеріал:").grid(row=6, column=0, sticky="w", padx=5, pady=5) # Мітка для матеріалу.
        self.materials = ("Шкіра", "Гума", "Синтетика") # Кортеж матеріалів.
        self.selected_material = tk.StringVar(value=self.materials[0]) # Створює змінну StringVar для зберігання обраного матеріалу.  Початкове значення - перший елемент кортежу.
        tk.OptionMenu(self.input_tab, self.selected_material, *self.materials).grid(row=6, column=1, padx=5, pady=5) # Створює випадаючий список для вибору матеріалу.

        tk.Label(self.input_tab, text="Рік випуску:").grid(row=7, column=0, sticky="w", padx=5, pady=5) # Мітка для року випуску.
        self.years = ("2020", "2021", "2022", "2023", "2024") # Кортеж років.
        self.selected_year = tk.StringVar(value=self.years[0]) # Змінна для обраного року.
        tk.OptionMenu(self.input_tab, self.selected_year, *self.years).grid(row=7, column=1, padx=5, pady=5) # Випадаючий список для року.

        tk.Label(self.input_tab, text="Країна виробництва:").grid(row=8, column=0, sticky="w", padx=5, pady=5) # Мітка для країни.
        self.countries = ("Україна", "США", "Китай", "Німеччина") # Кортеж країн.
        self.selected_country = tk.StringVar(value=self.countries[0]) # Змінна для обраної країни.
        tk.OptionMenu(self.input_tab, self.selected_country, *self.countries).grid(row=8, column=1, padx=5, pady=5) # Випадаючий список для країни.

        tk.Label(self.input_tab, text="Новий виробник:").grid(row=9, column=0, sticky="w", padx=5, pady=5) # Мітка для нового виробника.
        self.new_manufacturer_entry = tk.Entry(self.input_tab) # Поле вводу для назви нового виробника.
        self.new_manufacturer_entry.grid(row=9, column=1, padx=5, pady=5)

        # Кнопки для управління списком виробників.
        tk.Button(self.input_tab, text="➕ Додати", command=lambda: ListboxManager.add_item(self.manufacturer_listbox, self.new_manufacturer_entry)).grid(row=10, column=1, pady=2) # Кнопка "Додати".
        tk.Button(self.input_tab, text="✏️ Редагувати", command=lambda: ListboxManager.edit_item(self.manufacturer_listbox, self.new_manufacturer_entry)).grid(row=11, column=0, columnspan=2, pady=2) # Кнопка "Редагувати". columnspan=2 об'єднує дві комірки по горизонталі.
        tk.Button(self.input_tab, text="🗑️ Видалити", command=lambda: ListboxManager.delete_item(self.manufacturer_listbox)).grid(row=12, column=0, columnspan=2, pady=2) # Кнопка "Видалити".
        tk.Button(self.input_tab, text="🔃 Сортувати", command=lambda: ListboxManager.sort_items(self.manufacturer_listbox)).grid(row=11, column=1, columnspan=2, pady=2) # Кнопка "Сортувати".
        tk.Button(self.input_tab, text="↩️ Зворотній порядок", command=lambda: ListboxManager.reverse_items(self.manufacturer_listbox)).grid(row=12, column=1, columnspan=2, pady=2) # Кнопка "Зворотній порядок".

        self.image_display_label = tk.Label(self.input_tab) # Місце для відображення обраного зображення.
        self.image_display_label.grid(row=13, column=0, columnspan=3, pady=10)

        tk.Button(self.input_tab, text="✅ Створити об'єкт", command=self.control.create_soccer_ball).grid(row=15, column=1, pady=2) # Кнопка "Створити об'єкт".  Викликає метод create_soccer_ball() об'єкта control при натисканні.

    def build_output_tab(self):
        """
        Створює та розміщує віджети на вкладці "Інформація".
        Віджети включають мітки для відображення інформації про створений об'єкт та кнопки для навігації між об'єктами.
        """
        self.result_label = tk.Label(self.obj_tab, text="", font=("Arial", 12), justify=tk.CENTER) # Мітка для виведення текстової інформації про об'єкт.
        self.result_label.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky="ew") # Розміщення мітки. sticky="ew" розтягує мітку по горизонталі.

        self.result_image_label = tk.Label(self.obj_tab) # Мітка для відображення зображення об'єкта.
        self.result_image_label.grid(row=1, column=0, columnspan=3, padx=5, sticky="ew")

        # Додавання вибору джерела даних
        tk.Label(self.obj_tab, text="Джерело даних:").grid(row=2, column=0, sticky="w", padx=5, pady=5) # Мітка "Джерело даних".
        self.source_var = tk.StringVar(value="json") # Змінна для зберігання обраного джерела даних.  Початкове значення - "json".
        sources = ("JSON", "TXT", "CSV", "BIN") # Кортеж доступних джерел даних.
        tk.OptionMenu(self.obj_tab, self.source_var, *sources, command=self.control.load_objects_from_source).grid(row=2, column=1, columnspan=2, padx=5, pady=5) # Випадаючий список для вибору джерела.  При зміні значення викликається метод load_objects_from_source() об'єкта control.

        # Мітка для відображення поточного джерела даних.
        self.data_source_label = tk.Label(self.obj_tab, text="Джерело даних: JSON", font=("Arial", 10), justify=tk.CENTER)
        self.data_source_label.grid(row=3, column=0, columnspan=3, padx=5, pady=2, sticky="ew")

        # Кнопки для навігації та видалення об'єктів.
        ttk.Button(self.obj_tab, text="⬅️ Попередній об'єкт", command=self.control.show_previous_loaded_object).grid(row=4, column=0, padx=10, pady=5, sticky="w") # Кнопка "Попередній".
        ttk.Button(self.obj_tab, text="➡️ Наступний об'єкт", command=self.control.show_next_loaded_object).grid(row=4, column=2, padx=10, pady=5, sticky="e") # Кнопка "Наступний".
        ttk.Button(self.obj_tab, text="🗑️ Видалити об'єкт", command=self.control.delete_current_object, width=20).grid(row=5, column=0, columnspan=3, padx=10, sticky="ew") # Кнопка "Видалити".

    def update_result_image(self, image_path):
        """
        Оновлює відображення зображення на вкладці "Інформація".

        Args:
            image_path (str): Шлях до файлу зображення.
        """
        try:
            img = Image.open(image_path) # Відкриває зображення за вказаним шляхом.
            img = img.resize((250, 150)) # Змінює розмір зображення до 250x150 пікселів.
            self.tk_result_img = ImageTk.PhotoImage(img) # Перетворює зображення PIL у формат, придатний для відображення в tkinter.
            self.result_image_label.config(image=self.tk_result_img, text="") # Встановлює зображення у мітку та очищає текст мітки.
            self.result_image_label.image = self.tk_result_img # Зберігає посилання на об'єкт PhotoImage, щоб запобігти його видаленню збирачем сміття.
        except Exception as e: # Обробляє можливі помилки при відкритті або обробці зображення.
            self.result_image_label.config(image='', text=f"❌ {e}") # Виводить символ "X" та повідомлення про помилку у мітці.

    def set_gallery_view(self, view):
        """
        Встановлює об'єкт GalleryView для подальшої взаємодії з ним.

        Args:
            view (GalleryView): Об'єкт класу GalleryView.
        """
        self.view = view # Зберігає посилання на об'єкт GalleryView.
        self.view.image_label = self.image_display_label # Передає мітці GalleryView, в якій відображаються зображення.
        # Створює кнопки для перегортання зображень в галереї.
        tk.Button(self.input_tab, text="⬅️ Попереднє", command=self.view.prev_image).grid(row=14, column=0, padx=10)
        tk.Button(self.input_tab, text="➡️ Наступне", command=self.view.next_image).grid(row=14, column=2, padx=10)

    def update_data_source(self, source):
        """
        Оновлює текст мітки, що відображає поточне джерело даних.

        Args:
            source (str): Назва джерела даних ("JSON", "TXT", "CSV" або "BIN").
        """
        self.data_source_label.config(text=f"Джерело даних: {source}") # Оновлює текст мітки.
