from tkinter import *
from src.org.example.entity.Football import Football
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Спортивний інвентар - ⚽ Футбольний м'яч")
        self.root.geometry("900x700")

        # Ввід атрибутів у вікно
        Label(root, text="Назва:").pack()
        self.name_entry = Entry(root)
        self.name_entry.pack()

        Label(root, text="Ціна (грн):").pack()
        self.price_entry = Entry(root)
        self.price_entry.pack()

        Label(root, text="Вага (кг):").pack()
        self.weight_entry = Entry(root)
        self.weight_entry.pack()

        Label(root, text="Діаметр (см):").pack()
        self.diameter_entry = Entry(root)
        self.diameter_entry.pack()

        Label(root, text="Тиск (атм):").pack()
        self.pressure_entry = Entry(root)
        self.pressure_entry.pack()

        Button(root, text="Створити об'єкт", command=self.create_object).pack(pady=10)

        self.result_label = Label(root, text="", justify=LEFT, font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Галерея зображень
        self.image_paths = ["../../../resource/img/ball1.png", "../../../resource/img/ball2.png", "../../../resource/img/ball3.png"]
        self.current_index = 0

        self.image_label = Label(root)
        self.image_label.pack(pady=10)
        self.show_image()

        Button(root, text="⬅️ Попереднє", command=self.prev_image).pack(side=LEFT, padx=20)
        Button(root, text="➡️ Наступне", command=self.next_image).pack(side=RIGHT, padx=20)

    def create_object(self):
        try:
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            weight = float(self.weight_entry.get())
            diameter = float(self.diameter_entry.get())
            pressure = float(self.pressure_entry.get())

            self.football = Football(name, price, weight, diameter, pressure)
            self.result_label.config(text=self.football.getInfo())

        except ValueError:
            self.result_label.config(text="❌ Помилка: перевірте введені дані!")

    def show_image(self):
        try:
            img = Image.open(self.image_paths[self.current_index])
            img = img.resize((350, 250))
            self.tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_img)
        except Exception as e:
            self.image_label.config(text=f"Помилка завантаження зображення\n{e}")

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.show_image()

    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_paths)
        self.show_image()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
