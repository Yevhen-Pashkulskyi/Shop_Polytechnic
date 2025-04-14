class SportsEquipment:
    def __init__(self, name, price, weight):
        self.name = name # назва
        self.price = price # ціна
        self.weight = weight # вага

 # вивід значень
    def getInfo(self):
        return f"Назва: {self.name}\nЦіна: {self.price} грн.\nВага: {self.weight} кг"
