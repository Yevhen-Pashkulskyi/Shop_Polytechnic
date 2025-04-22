from src.org.example.control.Control import Control
from tkinter import *

# інтерфейс тобто вікно для відображення даних та управління програмою
class GUIBuilder:
    def __init__(self, root, view):
        self.root = root
        self.view = view
        self.control = Control(self)

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

        self.result_label = Label(root, text="", justify=LEFT, font=("Arial", 12))
        self.result_label.pack(pady=10)

        Button(root, text="Створити об'єкт", command=self.control.create_soccer_ball).pack(pady=10)

        Button(root, text="⬅️ Попереднє", command=self.view.prev_image).pack(side=LEFT, padx=20)
        Button(root, text="➡️ Наступне", command=self.view.next_image).pack(side=RIGHT, padx=20)
