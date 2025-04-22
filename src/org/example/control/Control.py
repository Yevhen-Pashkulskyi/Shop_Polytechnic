from tkinter import messagebox

from src.org.example.model.CreateObj import CreateObj


class Control:
    def __init__(self, gui):
        self.gui = gui

    def create_soccer_ball(self):
        try:
            name = self.gui.name_entry.get()
            price = float(self.gui.price_entry.get())
            weight = float(self.gui.weight_entry.get())
            diameter = float(self.gui.diameter_entry.get())
            pressure = float(self.gui.pressure_entry.get())  # window

            soccer_ball = CreateObj.create_soccer_ball(name, price, weight, diameter, pressure)
            self.gui.result_label.config(text=soccer_ball.getInfo())

        except ValueError:
            # self.result_label.config(text="❌ Помилка: перевірте введені дані!")
            messagebox.showerror("Помилка", "❌ Перевірте введені числові значення!")
        except Exception as e:
            messagebox.showerror("Помилка", f"⚠️ Помилка: {e}")
