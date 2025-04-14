from src.org.example.model.CreateObj import CreateObj


class WindowsWork:
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

        create_obj = CreateObj

        Button(root, text="Створити об'єкт", command=self.createoj.create_object).pack(pady=10)