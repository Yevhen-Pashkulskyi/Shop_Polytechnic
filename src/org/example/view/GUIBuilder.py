import os
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from src.org.example.control.Control import Control
from tkinter import *
from src.org.example.view.ListBoxManager import ListboxManager


# інтерфейс тобто вікно для відображення даних та управління програмою
class GUIBuilder:
    def __init__(self, root):
        self.tk_result_img = None
        self.root = root
        self.view = None
        self.control = Control(self)

        self.root.title("Спортивний інвентар - ⚽ Футбольний м'яч")
        self.root.geometry("700x900")

        self.notebook = ttk.Notebook(self.root)
        # вкладка для вводу даних
        self.input_tab = Frame(self.notebook)
        self.notebook.add(self.input_tab, text="Ввід даних")
        # вкладка для вивіду даних
        self.obj_tab = Frame(self.notebook)
        self.notebook.add(self.obj_tab, text="Інформація")
        self.notebook.pack(fill="both", expand=True)

        # Ввід атрибутів у вікно
        # назва
        Label(self.input_tab, text="Назва:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = Entry(self.input_tab, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        # ціна
        Label(self.input_tab, text="Ціна (грн):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.price_entry = Entry(self.input_tab, width=10)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)
        # вага
        Label(self.input_tab, text="Вага (кг):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.weight_entry = Entry(self.input_tab, width=10)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(self.input_tab, text="Діаметр (см):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.diameter_entry = Entry(self.input_tab, width=10)
        self.diameter_entry.grid(row=3, column=1, padx=5, pady=5)

        Label(self.input_tab, text="Тиск (атм):").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.pressure_entry = Entry(self.input_tab, width=10)
        self.pressure_entry.grid(row=4, column=1, padx=5, pady=5)

        # --- Виробник (Listbox + scrollbar)
        Label(self.input_tab, text="Виробник:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.manufacturer_listbox = Listbox(self.input_tab, height=4, exportselection=False)
        self.manufacturer_scroll = Scrollbar(self.input_tab, orient=VERTICAL,
                                             command=self.manufacturer_listbox.yview)
        self.manufacturer_listbox.config(yscrollcommand=self.manufacturer_scroll.set)
        self.manufacturer_listbox.grid(row=5, column=1, padx=5, pady=5)
        self.manufacturer_scroll.grid(row=5, column=2, sticky="ns", padx=0)
        self.manufacturers = []  # ["Adidas", "Nike", "Puma"]
        for item in self.manufacturers:
            self.manufacturer_listbox.insert(END, item)

        # --- Матеріал (OptionMenu)
        Label(self.input_tab, text="Матеріал:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.materials = ("Шкіра", "Гума", "Синтетика")
        self.selected_material = StringVar()
        self.selected_material.set(self.materials[0])
        OptionMenu(self.input_tab, self.selected_material,
                   *self.materials).grid(row=6, column=1, padx=5, pady=5)

        # --- Рік випуску (OptionMenu з кортежу)
        Label(self.input_tab, text="Рік випуску:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.years = ("2020", "2021", "2022", "2023", "2024")
        self.selected_year = StringVar()
        self.selected_year.set(self.years[0])
        OptionMenu(self.input_tab, self.selected_year,
                   *self.years).grid(row=7, column=1, padx=5, pady=5)

        # --- Країна (OptionMenu з кортежу)
        Label(self.input_tab, text="Країна виробництва:").grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.countries = ("Україна", "США", "Китай", "Німеччина")
        self.selected_country = StringVar()
        self.selected_country.set(self.countries[0])
        OptionMenu(self.input_tab, self.selected_country,
                   *self.countries).grid(row=8, column=1, padx=5, pady=5)

        # Для ввода і редагування виробників
        Label(self.input_tab, text="Новий виробник:").grid(row=9, column=0, sticky="w", padx=5, pady=5)
        self.new_manufacturer_entry = Entry(self.input_tab)
        self.new_manufacturer_entry.grid(row=9, column=1, padx=5, pady=5)

        # Кнопки керування списком
        (Button(self.input_tab, text="➕ Додати",
                command=lambda: ListboxManager.add_item(self.manufacturer_listbox,
                                                        self.new_manufacturer_entry)).grid(row=10, column=0, padx=5,
                                                                                           pady=2))
        Button(self.input_tab, text="✏️ Редагувати",
               command=lambda: ListboxManager.edit_item(self.manufacturer_listbox,
                                                        self.new_manufacturer_entry)).grid(row=10, column=1, padx=5,
                                                                                           pady=2)
        Button(self.input_tab, text="🗑️ Видалити",
               command=lambda: ListboxManager.delete_item(self.manufacturer_listbox)).grid(row=11, column=0, padx=5,
                                                                                           pady=2)
        Button(self.input_tab, text="🔃 Сортувати",
               command=lambda: ListboxManager.sort_items(self.manufacturer_listbox)).grid(row=11, column=1, padx=5,
                                                                                          pady=2)
        Button(self.input_tab, text="↩️ Зворотній порядок",
               command=lambda: ListboxManager.reverse_items(self.manufacturer_listbox)).grid(row=12, column=0, padx=5,
                                                                                             pady=2)
        Button(self.input_tab, text="ℹ️ Перевірити розмір",
               command=lambda: ListboxManager.check_list_size(self.manufacturer_listbox, limit=5)).grid(row=12,
                                                                                                        column=1,
                                                                                                        padx=5, pady=2)

        # кнопка створити об'єкт
        Button(self.input_tab, text="✅ Створити об'єкт",
               command=self.control.create_soccer_ball).grid(row=14, column=0,
                                                             columnspan=3, pady=15)

        self.result_label = Label(self.obj_tab, text="", justify=LEFT, font=("Arial", 12))
        self.result_label.pack(anchor="nw", padx=10, pady=10)

        self.result_image_label = Label(self.obj_tab)
        self.result_image_label.pack(pady=10)

    def update_result_image(self, image_path):
        try:
            print("Путь к изображению:", image_path)
            print("Существует ли файл:", os.path.exists(image_path))
            print("Текущая рабочая директория:", os.getcwd())

            img = Image.open(image_path)
            img = img.resize((250, 150))
            self.tk_result_img = ImageTk.PhotoImage(img)
            self.result_image_label.config(image=self.tk_result_img, text="")
            print(f"[✅] Зображення завантажено: {image_path}")

        except Exception as e:
            print(f"[❌] Помилка завантаження зображення: {e}")
            self.result_image_label.config(image='', text="❌ Не вдалося завантажити зображення")

    def set_gallery_view(self, view):
        self.view = view
        # зображення перемикати
        Button(self.input_tab, text="⬅️ Попереднє",
               command=self.view.prev_image).grid(row=13, column=0, padx=10)
        Button(self.input_tab, text="➡️ Наступне",
               command=self.view.next_image).grid(row=13, column=1, padx=10)
