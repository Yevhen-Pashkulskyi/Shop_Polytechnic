import os # Імпортуємо модуль os для роботи з операційною системою, зокрема для перевірки існування файлів.
import tkinter as tk # Імпортуємо бібліотеку tkinter під псевдонімом tk для створення базових GUI-елементів.
from tkinter import messagebox, ttk # Імпортуємо модуль messagebox для відображення діалогових вікон
# та модуль ttk для стилізованих віджетів tkinter.
from PIL import Image, ImageTk # Імпортуємо класи Image та ImageTk з бібліотеки Pillow для роботи із зображеннями.
from src.org.example.control.Control import Control # Імпортуємо клас Control, що відповідає за логіку обробки подій GUI.
from src.org.example.view.ListBoxManager import ListboxManager # Імпортуємо клас ListboxManager для керування списками.
from src.org.example.model.ObjSaver import ObjectSaver # Імпортуємо клас ObjectSaver для завантаження збережених об'єктів.


# інтерфейс тобто вікно для відображення даних та управління програмою
class GUIBuilder:
    """
    Клас, що відповідає за побудову графічного інтерфейсу програми.
    """
    def __init__(self, root):
        """
        Конструктор класу GUIBuilder.

        Args:
            root (tkinter.Tk): Основний віконний контейнер tkinter, в якому буде розміщено весь GUI.
        """
        self.tk_result_img = None # Атрибут для зберігання об'єкта PhotoImage відображеного зображення результату.
        # Початково встановлюється в None.
        self.root = root # Зберігаємо посилання на основне вікно tkinter (root).
        self.view = None # Атрибут для зберігання посилання на об'єкт GalleryView.
        # Ініціалізується як None та встановлюється пізніше.
        self.control = Control(self) # Створюємо екземпляр класу Control, передаючи йому поточний об'єкт GUIBuilder (self).
        # Це дозволяє Control взаємодіяти з елементами GUI.
        self.loaded_objects = [] # Атрибут для зберігання списку завантажених об'єктів Ball з файлу.
        self.current_loaded_object_index = 0 # Атрибут для відстеження індексу поточного об'єкта,
        # що відображається у вкладці "Інформація".

        self.root.title("Спортивний інвентар - ⚽🛹🏓🛼🎾") # Встановлюємо заголовок головного вікна.
        self.root.geometry("550x950") # Встановлюємо початковий розмір головного вікна (ширина x висота).

        self.notebook = ttk.Notebook(self.root) # Створюємо віджет Notebook (панель з вкладками) у головному вікні.
        # вкладка для вводу даних
        self.input_tab = tk.Frame(self.notebook) # Створюємо фрейм (контейнер) для вкладки "Ввід даних".
        self.notebook.add(self.input_tab, text="Ввід даних") # Додаємо вкладку "Ввід даних" до Notebook.
        # вкладка для вивіду даних
        self.obj_tab = tk.Frame(self.notebook) # Створюємо фрейм для вкладки "Інформація".
        self.notebook.add(self.obj_tab, text="Інформація") # Додаємо вкладку "Інформація" до Notebook.
        self.notebook.pack(fill="both", expand=True) # Розміщуємо Notebook у головному вікні,
        # заповнюючи доступний простір в обох напрямках (fill="both")
        # та дозволяючи йому розширюватися при зміні розміру вікна (expand=True).

        # Ввід атрибутів у вікно (вкладка "Ввід даних")
        # назва
        tk.Label(self.input_tab, text="Назва:").grid(row=0, column=0, sticky="w", padx=5, pady=5) # Створюємо мітку "Назва:"
        # та розміщуємо її у сітці.
        # sticky="w" - притискання до західної сторони комірки.
        # padx, pady - відступи.
        self.name_entry = tk.Entry(self.input_tab, width=20) # Створюємо поле введення для назви.
        self.name_entry.grid(row=0, column=1, padx=5, pady=5) # Розміщуємо поле введення назви у сітці.
        # ціна
        tk.Label(self.input_tab, text="Ціна (грн):").grid(row=1, column=0, sticky="w", padx=5, pady=5) # Мітка для ціни.
        self.price_entry = tk.Entry(self.input_tab, width=10) # Поле введення для ціни.
        self.price_entry.grid(row=1, column=1, padx=5, pady=5) # Розміщення поля ціни.
        # вага
        tk.Label(self.input_tab, text="Вага (кг):").grid(row=2, column=0, sticky="w", padx=5, pady=5) # Мітка для ваги.
        self.weight_entry = tk.Entry(self.input_tab, width=10) # Поле введення для ваги.
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5) # Розміщення поля ваги.

        tk.Label(self.input_tab, text="Діаметр (см):").grid(row=3, column=0, sticky="w", padx=5, pady=5) # Мітка для діаметра.
        self.diameter_entry = tk.Entry(self.input_tab, width=10) # Поле введення для діаметра.
        self.diameter_entry.grid(row=3, column=1, padx=5, pady=5) # Розміщення поля діаметра.

        tk.Label(self.input_tab, text="Тиск (атм):").grid(row=4, column=0, sticky="w", padx=5, pady=5) # Мітка для тиску.
        self.pressure_entry = tk.Entry(self.input_tab, width=10) # Поле введення для тиску.
        self.pressure_entry.grid(row=4, column=1, padx=5, pady=5) # Розміщення поля тиску.

        # --- Виробник (Listbox + scrollbar)
        tk.Label(self.input_tab, text="Виробник:").grid(row=5, column=0, sticky="w", padx=5, pady=5) # Мітка "Виробник:".
        self.manufacturer_listbox = tk.Listbox(self.input_tab, height=4, width=10, exportselection=False) # Створюємо список (Listbox)
        # для вибору виробника.
        # height - висота в рядках, width - ширина в символах,
        # exportselection=False - відключає передачу виділення іншим віджетам.
        self.manufacturer_scroll = tk.Scrollbar(self.input_tab, orient=tk.VERTICAL, # Створюємо вертикальний скролбар.
                                                command=self.manufacturer_listbox.yview) # Встановлюємо команду для скролбара,
        # яка буде змінювати вертикальний виджет списку.
        self.manufacturer_listbox.config(yscrollcommand=self.manufacturer_scroll.set) # Налаштовуємо вертикальну прокрутку списку,
        # пов'язуючи її зі скролбаром.
        self.manufacturer_listbox.grid(row=5, column=1, padx=5, pady=5) # Розміщуємо список виробників у сітці.
        self.manufacturer_scroll.grid(row=5, column=2, sticky="ns", padx=0) # Розміщуємо скролбар у сітці,
        # sticky="ns" - розтягування по вертикалі.
        self.manufacturers = ["Adidas", "Nike", "Puma"] # Список початкових виробників.
        for item in self.manufacturers:
            self.manufacturer_listbox.insert(tk.END, item) # Додаємо початкових виробників до списку. tk.END - вставляє в кінець списку.

        # --- Матеріал (OptionMenu)
        tk.Label(self.input_tab, text="Матеріал:").grid(row=6, column=0, sticky="w", padx=5, pady=5) # Мітка "Матеріал:".
        self.materials = ("Шкіра", "Гума", "Синтетика") # Кортеж доступних матеріалів.
        self.selected_material = tk.StringVar() # Створюємо змінну tkinter для зберігання вибраного матеріалу.
        self.selected_material.set(self.materials[0]) # Встановлюємо початкове значення вибраного матеріалу.
        tk.OptionMenu(self.input_tab, self.selected_material, # Створюємо випадаючий список (OptionMenu).
                      *self.materials).grid(row=6, column=1, padx=5, pady=5) # Розміщуємо випадаючий список матеріалів.
        # * перед кортежем розпаковує його елементи як окремі аргументи для OptionMenu.

        # --- Рік випуску (OptionMenu з кортежу)
        tk.Label(self.input_tab, text="Рік випуску:").grid(row=7, column=0, sticky="w", padx=5, pady=5) # Мітка "Рік випуску:".
        self.years = ("2020", "2021", "2022", "2023", "2024") # Кортеж доступних років випуску.
        self.selected_year = tk.StringVar() # Змінна tkinter для зберігання вибраного року.
        self.selected_year.set(self.years[0]) # Встановлюємо початковий рік.
        tk.OptionMenu(self.input_tab, self.selected_year, # Випадаючий список років.
                      *self.years).grid(row=7, column=1, padx=5, pady=5) # Розміщення списку років.

        # --- Країна (OptionMenu з кортежу)
        tk.Label(self.input_tab, text="Країна виробництва:").grid(row=8, column=0, sticky="w", padx=5, pady=5) # Мітка "Країна виробництва:".
        self.countries = ("Україна", "США", "Китай", "Німеччина") # Кортеж доступних країн.
        self.selected_country = tk.StringVar() # Змінна tkinter для зберігання вибраної країни.
        self.selected_country.set(self.countries[0]) # Встановлюємо початкову країну.
        tk.OptionMenu(self.input_tab, self.selected_country, # Випадаючий список країн.
                      *self.countries).grid(row=8, column=1, padx=5, pady=5) # Розміщення списку країн.

        # Для ввода і редагування виробників
        tk.Label(self.input_tab, text="Новий виробник:").grid(row=9, column=0, sticky="w", padx=5, pady=5) # Мітка для введення нового виробника.
        self.new_manufacturer_entry = tk.Entry(self.input_tab) # Поле введення для нового виробника.
        self.new_manufacturer_entry.grid(row=9, column=1, padx=5, pady=5) # Розміщення поля введення нового виробника.

        # Кнопки керування списком виробників
        (tk.Button(self.input_tab, text="➕ Додати", # Кнопка "Додати".
                   command=lambda: ListboxManager.add_item(self.manufacturer_listbox, # Команда при натисканні - виклик
                                                           self.new_manufacturer_entry)).grid(row=10, column=1, padx=5, # статичного методу add_item
                                                                                              pady=2)) # класу ListboxManager.
        tk.Button(self.input_tab, text="✏️ Редагувати", # Кнопка "Редагувати".
                  command=lambda: ListboxManager.edit_item(self.manufacturer_listbox, # Виклик статичного методу edit_item.
                                                           self.new_manufacturer_entry)).grid(row=11, column=0, padx=2,
                                                                                              columnspan=2, pady=2)
        tk.Button(self.input_tab, text="🗑️ Видалити", # Кнопка "Видалити".
                  command=lambda: ListboxManager.delete_item(self.manufacturer_listbox)).grid(row=12, column=0, padx=5, # Виклик статичного методу delete_item.
                                                                                              columnspan=2, pady=2)
        tk.Button(self.input_tab, text="🔃 Сортувати", # Кнопка "Сортувати".
                  command=lambda: ListboxManager.sort_items(self.manufacturer_listbox)).grid(row=11, column=1, padx=5, # Виклик статичного методу sort_items.
                                                                                             columnspan=2, pady=2)
        tk.Button(self.input_tab, text="↩️ Зворотній порядок", # Кнопка "Зворотній порядок".
                  command=lambda: ListboxManager.reverse_items(self.manufacturer_listbox)).grid(row=12, column=1, padx=1, # Виклик статичного методу reverse_items.
                                                                                                columnspan=2, pady=2)

        # Галерея (зображення у вкладці "Ввід даних")
        self.image_display_label = tk.Label(self.input_tab) # Мітка для відображення зображення галереї.
        self.image_display_label.grid(row=13, column=0, columnspan=3, pady=10) # Розміщення мітки галереї.

        # кнопка створити об'єкт
        tk.Button(self.input_tab, text="✅ Створити об'єкт", # Кнопка "Створити об'єкт".
                  command=self.control.create_soccer_ball).grid(row=15, column=1, # Команда - виклик методу create_soccer_ball
                                                                pady=2) # об'єкта Control (self.control).

        # Елементи вкладки "Інформація"
        self.result_label = tk.Label(self.obj_tab, text="", justify=tk.LEFT, font=("Arial", 12)) # Мітка для відображення текстової інформації про об'єкт.
        # justify=tk.LEFT - вирівнювання тексту по лівому краю.
        # font - шрифт тексту.
        self.result_label.pack(anchor="nw", padx=10, pady=10) # Розміщення мітки результату. anchor="nw" - притискання до північно-західного кута.

        self.result_image_label = tk.Label(self.obj_tab) # Мітка для відображення зображення об'єкта.
        self.result_image_label.pack(pady=10) # Розміщення мітки зображення результату.

        # Кнопки для перемикання між завантаженими об'єктами у вкладці "Інформація"
        prev_obj_button = ttk.Button(self.obj_tab, text="⬅️ Попередній об'єкт", command=self.show_previous_loaded_object) # Кнопка "Попередній об'єкт".
        prev_obj_button.pack(side="left", padx=10, pady=5) # Розміщення кнопки зліва.

        next_obj_button = ttk.Button(self.obj_tab, text="➡️ Наступний об'єкт", command=self.show_next_loaded_object) # Кнопка "Наступний об'єкт".
        next_obj_button.pack(side="right", padx=10, pady=5) # Розміщення кнопки справа.

        self.load_and_display_objects() # Викликаємо метод для завантаження та відображення збережених об'єктів при ініціалізації GUI.

    def load_and_display_objects(self):
        """
        Метод для завантаження всіх збережених об'єктів Ball з файлу та відображення першого з них
        у вкладці "Інформація".
        """
        self.loaded_objects = ObjectSaver.load_all() # Викликаємо статичний метод load_all() класу ObjectSaver
        # для отримання списку завантажених об'єктів Ball.
        if self.loaded_objects: # Перевіряємо, чи є завантажені об'єкти.
            self.show_loaded_object(0) # Якщо є, викликаємо метод show_loaded_object() для відображення першого об'єкта (за індексом 0).
        else: # Якщо завантажених об'єктів немає.
            self.result_label.config(text="Ще не було створено жодного об'єкта.") # Встановлюємо відповідний текст у мітку результату.
            self.result_image_label.config(image='', text="") # Очищаємо мітку зображення результату.

    def show_loaded_object(self, index):
        """
        Метод для відображення інформації та зображення об'єкта Ball за вказаним індексом
        у вкладці "Інформація".

        Args:
            index (int): Індекс об'єкта у списку self.loaded_objects, який потрібно відобразити.
        """
        if 0 <= index < len(self.loaded_objects): # Перевіряємо, чи переданий індекс є валідним для списку завантажених об'єктів.
            obj = self.loaded_objects[index] # Отримуємо об'єкт Ball за вказаним індексом.
            self.result_label.config(text=obj.getInfo()) # Оновлюємо текст мітки результату інформацією про об'єкт,
            # отриманою за допомогою методу getInfo() об'єкта Ball.
            if obj.image_path: # Перевіряємо, чи об'єкт має шлях до зображення.
                self.update_result_image(obj.image_path) # Якщо є, викликаємо метод update_result_image() для відображення зображення.
            else: # Якщо шлях до зображення відсутній.
                self.result_image_label.config(image='', text="❌ Зображення відсутнє") # Встановлюємо повідомлення про відсутність зображення.
            self.current_loaded_object_index = index # Оновлюємо індекс поточного відображуваного об'єкта.

    def show_previous_loaded_object(self):
        """
        Метод для відображення попереднього завантаженого об'єкта у вкладці "Інформація".
        """
        if self.loaded_objects: # Перевіряємо, чи є завантажені об'єкти.
            self.current_loaded_object_index = (self.current_loaded_object_index - 1) % len(self.loaded_objects) # Зменшуємо індекс на 1,
            # використовуючи % для циклічного переходу.
            self.show_loaded_object(self.current_loaded_object_index) # Відображаємо об'єкт за новим індексом.

    def show_next_loaded_object(self):
        """
        Метод для відображення наступного завантаженого об'єкта у вкладці "Інформація".
        """
        if self.loaded_objects: # Перевіряємо, чи є завантажені об'єкти.
            self.current_loaded_object_index = (self.current_loaded_object_index + 1) % len(self.loaded_objects) # Збільшуємо індекс на 1,
            # використовуючи % для циклічного переходу.
            self.show_loaded_object(self.current_loaded_object_index) # Відображаємо об'єкт за новим індексом.

    def update_result_image(self, image_path):
        """
        Метод для завантаження та відображення зображення за вказаним шляхом
        у мітці зображення результату (self.result_image_label).

        Args:
            image_path (str): Шлях до файлу із зображенням.
        """
        try:
            img = Image.open(image_path) # Відкриваємо зображення за вказаним шляхом за допомогою Pillow.
            img = img.resize((250, 150)) # Змінюємо розмір зображення до 250x150 пікселів.
            self.tk_result_img = ImageTk.PhotoImage(img) # Створюємо об'єкт PhotoImage з зображення Pillow для відображення в tkinter.

            self.result_image_label.config(image=self.tk_result_img, text="") # Оновлюємо віджет image_label, встановлюючи йому нове зображення
            # та очищаючи можливий попередній текст.
            self.result_image_label.image = self.tk_result_img # Зберігаємо посилання на об'єкт PhotoImage, щоб запобігти його видаленню
            # збирачем сміття tkinter.
            print(f"[✅] Зображення завантажено: {image_path}") # Виводимо повідомлення про успішне завантаження зображення в консоль.
        except Exception as e: # Обробляємо можливі помилки при завантаженні зображення.
            print(f"[❌] Помилка завантаження зображення: {e}") # Виводимо повідомлення про помилку в консоль.
            self.result_image_label.config(image='', text="❌ Не вдалося завантажити зображення") # Встановлюємо повідомлення про помилку у віджеті.

    def set_gallery_view(self, view):
        """
        Метод для встановлення посилання на об'єкт GalleryView та налаштування кнопок
        перемикання зображень у вкладці "Ввід даних".

        Args:
            view (GalleryView): Екземпляр класу GalleryView.
        """
        self.view = view # Зберігаємо посилання на об'єкт GalleryView у атрибуті self.view.
        self.view.image_label = self.image_display_label # Передаємо віджет для відображення зображень галереї
        # з GUIBuilder до GalleryView.
        # кнопки перемикання зображень у вкладці "Ввід даних"
        tk.Button(self.input_tab, text="⬅️ Попереднє", # Створюємо кнопку "⬅️ Попереднє".
                  command=self.view.prev_image).grid(row=14, column=0, padx=10) # Команда - виклик методу prev_image() об'єкта GalleryView.
        tk.Button(self.input_tab, text="➡️ Наступне", # Створюємо кнопку "➡️ Наступне".
                  command=self.view.next_image).grid(row=14, column=2, padx=10) # Команда - виклик методу next_image() об'єкта GalleryView.