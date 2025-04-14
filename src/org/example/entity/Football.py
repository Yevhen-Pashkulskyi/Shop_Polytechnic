from src.org.example.entity.SportsEquipment import SportsEquipment


class Football(SportsEquipment):
    def __init__(self, name, price, weight, diameter, pressure):
        super().__init__(name, price, weight)
        self.diameter = diameter  # діаметр
        self.pressure = pressure  # тиск

    def getInfo(self):
        return f"{super().getInfo()}\nДіаметр: {self.diameter} см\nТиск: {self.pressure} атм"
