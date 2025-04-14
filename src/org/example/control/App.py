from tkinter import *
from src.org.example.entity.Football import Football
from PIL import Image, ImageTk

from src.org.example.view.GalleryView import ImageWork


class App:
    def __init__(self, root):
        self.root = root
        # self.root.title("Спортивний інвентар - ⚽ Футбольний м'яч")
        # self.root.geometry("900x700")
        #
        # # Ввід атрибутів у вікно
        # Label(root, text="Назва:").pack()
        # self.name_entry = Entry(root)
        # self.name_entry.pack()
        #
        # Label(root, text="Ціна (грн):").pack()
        # self.price_entry = Entry(root)
        # self.price_entry.pack()
        #
        # Label(root, text="Вага (кг):").pack()
        # self.weight_entry = Entry(root)
        # self.weight_entry.pack()
        #
        # Label(root, text="Діаметр (см):").pack()
        # self.diameter_entry = Entry(root)
        # self.diameter_entry.pack()
        #
        # Label(root, text="Тиск (атм):").pack()
        # self.pressure_entry = Entry(root)
        # self.pressure_entry.pack()
        #
        # Button(root, text="Створити об'єкт", command=self.create_object).pack(pady=10)

        self.result_label = Label(root, text="", justify=LEFT, font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Галерея
        self.view = ImageWork(root)
        self.view.show_image()


        Button(root, text="⬅️ Попереднє", command=self.view.prev_image).pack(side=LEFT, padx=20)
        Button(root, text="➡️ Наступне", command=self.view.next_image).pack(side=RIGHT, padx=20)

    def create_object(self):
        try:
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            weight = float(self.weight_entry.get())
            diameter = float(self.diameter_entry.get())
            pressure = float(self.pressure_entry.get()) #window

            self.football = Football(name, price, weight, diameter, pressure)
            self.result_label.config(text=self.football.getInfo())

        except ValueError:
            self.result_label.config(text="❌ Помилка: перевірте введені дані!")


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
