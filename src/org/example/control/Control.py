from tkinter import messagebox

from src.org.example.model.CreateObj import CreateObj
from src.org.example.model.ObjSaver import ObjSaver


class Control:
    def __init__(self, gui):
        self.gui = gui

    def create_soccer_ball(self):
        try:
            name = self.gui.name_entry.get().strip()
            if not name:
                raise ValueError("⛔ Поле «Назва» не може бути порожнім.")

            price = self.get_float(self.gui.price_entry, "Ціна (грн)")
            weight = self.get_float(self.gui.weight_entry, "Вага (кг)")
            diameter = self.get_float(self.gui.diameter_entry, "Діаметр (см)")
            pressure = self.get_float(self.gui.pressure_entry, "Тиск (атм)")

            # Получаем выбранного производителя
            if self.gui.manufacturer_listbox.size() == 0:
                raise ValueError("⚠️ Список виробників не може бути порожнім.")

            manufacturer = self.get_selected_listbox_value(self.gui.manufacturer_listbox, "виробника")
            material = self.gui.selected_material.get()
            year = self.gui.selected_year.get()
            country = self.gui.selected_country.get()
            image_path = self.gui.view.get_current_image_path()

            ball = CreateObj.create_soccer_ball(name, price, weight, diameter, pressure,
                                                manufacturer, material, year, country,
                                               image_path)

            ObjSaver.save(ball)

            self.gui.result_label.config(text=ball.getInfo())
            self.gui.update_result_image(image_path)
            self.gui.load_and_display_objs()

        except ValueError as ve:
            messagebox.showerror("Помилка валідації", str(ve))
        except Exception as e:
            messagebox.showerror("Помилка", f"⚠️ Сталася непередбачена помилка:\n{e}")

    def get_selected_listbox_value(self, listbox, label):
        try:
            index = listbox.curselection()[0]
            return listbox.get(index)
        except IndexError:
            raise ValueError(f"⛔ Оберіть значення {label} зі списку.")

    # функция для проверки ввода на число и отрецательное число
    def get_float(self, entry, label_name):
        value = entry.get().strip()
        if not value:
            raise ValueError(f"⛔ Поле «{label_name}» не може бути порожнім.")
        try:
            float_value = float(value)
        except ValueError:
            raise ValueError(f"⛔ Поле «{label_name}» повинно містити число.")
        if float_value <= 0:
            raise ValueError(f"⛔ Значення «{label_name}» не може бути від'ємним.")
        return float_value
