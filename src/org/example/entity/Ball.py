from src.org.example.entity.SportsEquipment import SportsEquipment


class Ball(SportsEquipment):
    def __init__(self, name, price, weight, diameter, pressure,
                 manufacturer, material, year, country):
        super().__init__(name, price, weight)
        self.diameter = diameter  # діаметр
        self.pressure = pressure  # тиск
        # new values
        self.manufacturer = manufacturer  # виробник
        self.material = material  # матеріал
        self.year = year  # рік
        self.country = country  # країна


    def getInfo(self):
        return (f"{super().getInfo()}\n"
                f"Діаметр: {self.diameter} см\n"
                f"Тиск: {self.pressure} атм\n"
                f"Виробник: {self.manufacturer}\n"
                f"Матеріал: {self.material}\n"
                f"Рік випуску: {self.year}\n"
                f"Країна: {self.country}\n")
                # f"Зображення: {self.image_path}")
