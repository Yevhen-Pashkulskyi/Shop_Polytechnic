from tkinter import messagebox

from src.org.example.model.CreateObj import CreateObj


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

            soccer_ball = CreateObj.create_soccer_ball(name, price, weight, diameter, pressure)
            self.gui.result_label.config(text=soccer_ball.getInfo())

        except ValueError as ve:
            messagebox.showerror("Помилка валідації", str(ve))
        except Exception as e:
            messagebox.showerror("Помилка", f"⚠️ Сталася непередбачена помилка:\n{e}")



    def get_float(self, entry, label_name):
        value = entry.get().strip()
        if not value:
            raise ValueError(f"⛔ Поле «{label_name}» не може бути порожнім.")
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"⛔ Поле «{label_name}» повинно містити число.")
