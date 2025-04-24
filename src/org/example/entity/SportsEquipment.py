class SportsEquipment:
    """
    Базовий клас для представлення спортивного обладнання.
    """
    def __init__(self, name, price, weight):
        """
        Конструктор класу SportsEquipment.

        Args:
            name (str): Назва спортивного обладнання.
            price (float): Ціна спортивного обладнання.
            weight (float): Вага спортивного обладнання.
        """
        self.name = name # Назва спортивного обладнання (атрибут self.name).
        self.price = price # Ціна спортивного обладнання (атрибут self.price).
        self.weight = weight # Вага спортивного обладнання (атрибут self.weight).

    # вивід значень
    def getInfo(self):
        """
        Метод для отримання базової інформації про спортивне обладнання у вигляді рядка.

        Returns:
            str: Рядок з назвою, ціною та вагою обладнання.
        """
        return f"Назва: {self.name}\nЦіна: {self.price} грн.\nВага: {self.weight} кг"