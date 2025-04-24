import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from src.org.example.control.Control import Control
from src.org.example.model.ObjSaver import ObjSaver
from src.org.example.view.ListBoxManager import ListboxManager


# інтерфейс тобто вікно для відображення даних та управління програмою
class GUIBuilder:
    def __init__(self, root):
        self.tk_result_img = None
        self.root = root
        self.view = None
        self.control = Control(self)
        self.loaded_objects = []
        self.current_loaded_obj_index = 0

        self.root.title("Спортивний інвентар - ⚽🛹🏓🛼🎾")
        self.root.geometry("550x950")

        self.notebook = ttk.Notebook(self.root)
        # вкладка для вводу даних
        self.input_tab = tk.Frame(self.notebook)
        self.notebook.add(self.input_tab, text="Ввід даних")
        # вкладка для вивіду даних
        self.obj_tab = tk.Frame(self.notebook)
        self.notebook.add(self.obj_tab, text="Інформація")
        self.notebook.pack(fill="both", expand=True)

        # Ввід атрибутів у вікно
        # назва
        tk.Label(self.input_tab, text="Назва:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_tab, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        # ціна
        tk.Label(self.input_tab, text="Ціна (грн):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.price_entry = tk.Entry(self.input_tab, width=10)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)
        # вага
        tk.Label(self.input_tab, text="Вага (кг):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.weight_entry = tk.Entry(self.input_tab, width=10)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Діаметр (см):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.diameter_entry = tk.Entry(self.input_tab, width=10)
        self.diameter_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Тиск (атм):").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.pressure_entry = tk.Entry(self.input_tab, width=10)
        self.pressure_entry.grid(row=4, column=1, padx=5, pady=5)

        # --- Виробник (Listbox + scrollbar)
        tk.Label(self.input_tab, text="Виробник:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.manufacturer_listbox = tk.Listbox(self.input_tab, height=4, width=10, exportselection=False)
        self.manufacturer_scroll = tk.Scrollbar(self.input_tab, orient=tk.VERTICAL,
                                                command=self.manufacturer_listbox.yview)
        self.manufacturer_listbox.config(yscrollcommand=self.manufacturer_scroll.set)
        self.manufacturer_listbox.grid(row=5, column=1, padx=5, pady=5)
        self.manufacturer_scroll.grid(row=5, column=1, columnspan=2, sticky="ns", padx=0)
        self.manufacturers = ["Adidas", "Nike", "Puma"]
        for item in self.manufacturers:
            self.manufacturer_listbox.insert(tk.END, item)

        # --- Матеріал (OptionMenu)
        tk.Label(self.input_tab, text="Матеріал:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.materials = ("Шкіра", "Гума", "Синтетика")
        self.selected_material = tk.StringVar()
        self.selected_material.set(self.materials[0])
        tk.OptionMenu(self.input_tab, self.selected_material,
                      *self.materials).grid(row=6, column=1, padx=5, pady=5)

        # --- Рік випуску (OptionMenu з кортежу)
        tk.Label(self.input_tab, text="Рік випуску:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.years = ("2020", "2021", "2022", "2023", "2024")
        self.selected_year = tk.StringVar()
        self.selected_year.set(self.years[0])
        tk.OptionMenu(self.input_tab, self.selected_year,
                      *self.years).grid(row=7, column=1, padx=5, pady=5)

        # --- Країна (OptionMenu з кортежу)
        tk.Label(self.input_tab, text="Країна виробництва:").grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.countries = ("Україна", "США", "Китай", "Німеччина")
        self.selected_country = tk.StringVar()
        self.selected_country.set(self.countries[0])
        tk.OptionMenu(self.input_tab, self.selected_country,
                      *self.countries).grid(row=8, column=1, padx=5, pady=5)

        # Для ввода і редагування виробників
        tk.Label(self.input_tab, text="Новий виробник:").grid(row=9, column=0, sticky="w", padx=5, pady=5)
        self.new_manufacturer_entry = tk.Entry(self.input_tab)
        self.new_manufacturer_entry.grid(row=9, column=1, padx=5, pady=5)

        # Кнопки керування списком
        (tk.Button(self.input_tab, text="➕ Додати",
                   command=lambda: ListboxManager.add_item(self.manufacturer_listbox,
                                                           self.new_manufacturer_entry)).grid(row=10, column=1, padx=5,
                                                                                              pady=2))
        tk.Button(self.input_tab, text="✏️ Редагувати",
                  command=lambda: ListboxManager.edit_item(self.manufacturer_listbox,
                                                           self.new_manufacturer_entry)).grid(row=11, column=0, padx=2,
                                                                                              columnspan=2, pady=2)
        tk.Button(self.input_tab, text="🗑️ Видалити",
                  command=lambda: ListboxManager.delete_item(self.manufacturer_listbox)).grid(row=12, column=0, padx=5,
                                                                                              columnspan=2, pady=2)
        tk.Button(self.input_tab, text="🔃 Сортувати",
                  command=lambda: ListboxManager.sort_items(self.manufacturer_listbox)).grid(row=11, column=1, padx=5,
                                                                                             columnspan=2, pady=2)
        tk.Button(self.input_tab, text="↩️ Зворотній порядок",
                  command=lambda: ListboxManager.reverse_items(self.manufacturer_listbox)).grid(row=12, column=1,
                                                                                                padx=1,
                                                                                                columnspan=2, pady=2)

        # Галерея (зображення)
        self.image_display_label = tk.Label(self.input_tab)
        self.image_display_label.grid(row=13, column=0, columnspan=3, pady=10)

        # кнопка створити об'єкт
        tk.Button(self.input_tab, text="✅ Створити об'єкт",
                  command=self.control.create_soccer_ball).grid(row=15, column=1, pady=2)

        # Елементи вкладки "Інформація"
        self.result_label = tk.Label(self.obj_tab, text="", font=("Arial", 12), justify=tk.CENTER)
        self.result_label.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky="ew")

        self.result_image_label = tk.Label(self.obj_tab)
        self.result_image_label.grid(row=1, column=0, columnspan=3, padx=5, sticky="ew")


        prev_obj_button = ttk.Button(self.obj_tab, text="⬅️ Попередній об'єкт",
                                     command=self.show_previous_loaded_object)
        prev_obj_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        next_obj_button = ttk.Button(self.obj_tab, text="➡️ Наступний об'єкт", command=self.show_next_loaded_object)
        next_obj_button.grid(row=2, column=2, padx=10, pady=5, sticky="e")

        delete_obj_button = ttk.Button(self.obj_tab, text="🗑️ Видалити об'єкт", command=self.delete_current_object,
                                       width=20)
        delete_obj_button.grid(row=3, column=0, columnspan=3, padx=10, sticky="ew")

        self.load_and_display_objs()

    def load_and_display_objs(self):
        self.loaded_objects = ObjSaver.load_all()
        if self.loaded_objects:
            self.show_loaded_object(0)  # Показати перший об'єкт
        else:
            self.result_label.config(text="Ще не було створено жодного об'єкта.")
            self.result_image_label.config(image='', text="")

    def show_loaded_object(self, index):
        if 0 <= index < len(self.loaded_objects):
            obj = self.loaded_objects[index]
            self.result_label.config(text=obj.getInfo())
            if obj.image_path:
                self.update_result_image(obj.image_path)
            else:
                self.result_image_label.config(image='', text="❌ Зображення відсутнє")
            self.current_loaded_object_index = index

    def show_previous_loaded_object(self):
        if self.loaded_objects:
            self.current_loaded_object_index = (self.current_loaded_object_index - 1) % len(self.loaded_objects)
            self.show_loaded_object(self.current_loaded_object_index)

    def show_next_loaded_object(self):
        if self.loaded_objects:
            self.current_loaded_object_index = (self.current_loaded_object_index + 1) % len(self.loaded_objects)
            self.show_loaded_object(self.current_loaded_object_index)

    def delete_current_object(self):
        if self.loaded_objects:
            current_object = self.loaded_objects[self.current_loaded_object_index]
            if messagebox.askyesno("Підтвердження", f"Ви впевнені, що хочете видалити об'єкт '{current_object.name}'?"):
                if ObjSaver.delete(current_object.name):
                    messagebox.showinfo("Успішно", f"Об'єкт '{current_object.name}' видалено.")
                    self.load_and_display_objs()
                else:
                    messagebox.showerror("Помилка", f"Не вдалося видалити об'єкт '{current_object.name}'.")
        else:
            messagebox.showinfo("Інформація", "Немає об'єктів для видалення.")

    def update_result_image(self, image_path):
        try:
            # print("Путь к изображению:", image_path)
            # print("Существует ли файл:", os.path.exists(image_path))
            # print("Текущая рабочая директория:", os.getcwd())

            img = Image.open(image_path)
            img = img.resize((250, 150))
            self.tk_result_img = ImageTk.PhotoImage(img)

            self.result_image_label.config(image=self.tk_result_img, text="")
            self.result_image_label.image = self.tk_result_img
            print(f"[✅] Зображення завантажено: {image_path}")
        except Exception as e:
            print(f"[❌] Помилка завантаження зображення: {e}")
            self.result_image_label.config(image='', text="❌ Не вдалося завантажити зображення")

    def set_gallery_view(self, view):
        self.view = view
        self.view.image_label = self.image_display_label
        # зображення перемикати
        tk.Button(self.input_tab, text="⬅️ Попереднє",
                  command=self.view.prev_image).grid(row=14, column=0, padx=10)
        tk.Button(self.input_tab, text="➡️ Наступне",
                  command=self.view.next_image).grid(row=14, column=2, padx=10)
