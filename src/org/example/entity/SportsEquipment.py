class SportsEquipment:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def getInfo(self):
        return f"Назва: {self.name}\nЦіна: {self.price} грн.\nВага: {self.weight} кг"
