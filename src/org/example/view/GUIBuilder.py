import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from src.org.example.view.ListBoxManager import ListboxManager

class GUIBuilder:
    def __init__(self, root, control):
        self.tk_result_img = None
        self.root = root
        self.control = control
        self.view = None

        self.root.title("Спортивний інвентар - ⚽🛹🏓🛼🎾")
        self.root.geometry("550x950")

        self.notebook = ttk.Notebook(self.root)
        self.input_tab = tk.Frame(self.notebook)
        self.obj_tab = tk.Frame(self.notebook)
        self.notebook.add(self.input_tab, text="Ввід даних")
        self.notebook.add(self.obj_tab, text="Інформація")
        self.notebook.pack(fill="both", expand=True)

        self.build_input_tab()
        self.build_output_tab()

    def build_input_tab(self):
        tk.Label(self.input_tab, text="Назва:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_tab, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Ціна (грн):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.price_entry = tk.Entry(self.input_tab, width=10)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Вага (кг):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.weight_entry = tk.Entry(self.input_tab, width=10)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Діаметр (см):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.diameter_entry = tk.Entry(self.input_tab, width=10)
        self.diameter_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Тиск (атм):").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.pressure_entry = tk.Entry(self.input_tab, width=10)
        self.pressure_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Виробник:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.manufacturer_listbox = tk.Listbox(self.input_tab, height=4, width=10, exportselection=False)
        self.manufacturer_scroll = tk.Scrollbar(self.input_tab, orient=tk.VERTICAL, command=self.manufacturer_listbox.yview)
        self.manufacturer_listbox.config(yscrollcommand=self.manufacturer_scroll.set)
        self.manufacturer_listbox.grid(row=5, column=1, padx=5, pady=5)
        self.manufacturer_scroll.grid(row=5, column=2, sticky="ns")

        self.manufacturers = ["Adidas", "Nike", "Puma"]
        for item in self.manufacturers:
            self.manufacturer_listbox.insert(tk.END, item)

        tk.Label(self.input_tab, text="Матеріал:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.materials = ("Шкіра", "Гума", "Синтетика")
        self.selected_material = tk.StringVar(value=self.materials[0])
        tk.OptionMenu(self.input_tab, self.selected_material, *self.materials).grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Рік випуску:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.years = ("2020", "2021", "2022", "2023", "2024")
        self.selected_year = tk.StringVar(value=self.years[0])
        tk.OptionMenu(self.input_tab, self.selected_year, *self.years).grid(row=7, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Країна виробництва:").grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.countries = ("Україна", "США", "Китай", "Німеччина")
        self.selected_country = tk.StringVar(value=self.countries[0])
        tk.OptionMenu(self.input_tab, self.selected_country, *self.countries).grid(row=8, column=1, padx=5, pady=5)

        tk.Label(self.input_tab, text="Новий виробник:").grid(row=9, column=0, sticky="w", padx=5, pady=5)
        self.new_manufacturer_entry = tk.Entry(self.input_tab)
        self.new_manufacturer_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Button(self.input_tab, text="➕ Додати", command=lambda: ListboxManager.add_item(self.manufacturer_listbox, self.new_manufacturer_entry)).grid(row=10, column=1, pady=2)
        tk.Button(self.input_tab, text="✏️ Редагувати", command=lambda: ListboxManager.edit_item(self.manufacturer_listbox, self.new_manufacturer_entry)).grid(row=11, column=0, columnspan=2, pady=2)
        tk.Button(self.input_tab, text="🗑️ Видалити", command=lambda: ListboxManager.delete_item(self.manufacturer_listbox)).grid(row=12, column=0, columnspan=2, pady=2)
        tk.Button(self.input_tab, text="🔃 Сортувати", command=lambda: ListboxManager.sort_items(self.manufacturer_listbox)).grid(row=11, column=1, columnspan=2, pady=2)
        tk.Button(self.input_tab, text="↩️ Зворотній порядок", command=lambda: ListboxManager.reverse_items(self.manufacturer_listbox)).grid(row=12, column=1, columnspan=2, pady=2)

        self.image_display_label = tk.Label(self.input_tab)
        self.image_display_label.grid(row=13, column=0, columnspan=3, pady=10)

        tk.Button(self.input_tab, text="✅ Створити об'єкт", command=self.control.create_soccer_ball).grid(row=15, column=1, pady=2)

    def build_output_tab(self):
        self.result_label = tk.Label(self.obj_tab, text="", font=("Arial", 12), justify=tk.CENTER)
        self.result_label.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky="ew")

        self.result_image_label = tk.Label(self.obj_tab)
        self.result_image_label.grid(row=1, column=0, columnspan=3, padx=5, sticky="ew")

        # Adding source selection
        tk.Label(self.obj_tab, text="Джерело даних:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.source_var = tk.StringVar(value="json")
        sources = ("JSON", "TXT", "CSV", "BIN")
        tk.OptionMenu(self.obj_tab, self.source_var, *sources, command=self.control.load_objects_from_source).grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Adding label to show current data source
        self.data_source_label = tk.Label(self.obj_tab, text="Джерело даних: JSON", font=("Arial", 10), justify=tk.CENTER)
        self.data_source_label.grid(row=3, column=0, columnspan=3, padx=5, pady=2, sticky="ew")

        ttk.Button(self.obj_tab, text="⬅️ Попередній об'єкт", command=self.control.show_previous_loaded_object).grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ttk.Button(self.obj_tab, text="➡️ Наступний об'єкт", command=self.control.show_next_loaded_object).grid(row=4, column=2, padx=10, pady=5, sticky="e")
        ttk.Button(self.obj_tab, text="🗑️ Видалити об'єкт", command=self.control.delete_current_object, width=20).grid(row=5, column=0, columnspan=3, padx=10, sticky="ew")

    def update_result_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((250, 150))
            self.tk_result_img = ImageTk.PhotoImage(img)
            self.result_image_label.config(image=self.tk_result_img, text="")
            self.result_image_label.image = self.tk_result_img
        except Exception as e:
            self.result_image_label.config(image='', text=f"❌ {e}")

    def set_gallery_view(self, view):
        self.view = view
        self.view.image_label = self.image_display_label
        tk.Button(self.input_tab, text="⬅️ Попереднє", command=self.view.prev_image).grid(row=14, column=0, padx=10)
        tk.Button(self.input_tab, text="➡️ Наступне", command=self.view.next_image).grid(row=14, column=2, padx=10)

    def update_data_source(self, source):
        self.data_source_label.config(text=f"Джерело даних: {source}")