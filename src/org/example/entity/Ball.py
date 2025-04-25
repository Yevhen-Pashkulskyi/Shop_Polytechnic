from src.org.example.entity.SportsEquipment import SportsEquipment


class Ball(SportsEquipment):
    def __init__(self, name, price, weight, diameter, pressure,
                 manufacturer, material, year, country, image_path):
        super().__init__(name, price, weight)
        self.diameter = diameter
        self.pressure = pressure

        self.manufacturer = manufacturer
        self.material = material
        self.year = year
        self.country = country
        self.image_path = image_path

    def getInfo(self):
        return (f"{super().getInfo()}\n"
                f"Діаметр: {self.diameter} см\n"
                f"Тиск: {self.pressure} атм\n"
                f"Виробник: {self.manufacturer}\n"
                f"Матеріал: {self.material}\n"
                f"Рік випуску: {self.year}\n"
                f"Країна: {self.country}\n")
