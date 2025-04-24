from src.org.example.entity.SportsEquipment import SportsEquipment # Імпортуємо клас SportsEquipment з вказаного модуля.
# SportsEquipment, ймовірно, є базовим класом для різних видів
# спортивного обладнання, включаючи Ball.


class Ball(SportsEquipment):
    """
    Клас, що представляє футбольний м'яч.
    Наслідується від класу SportsEquipment.
    """
    def __init__(self, name, price, weight, diameter, pressure,
                 manufacturer, material, year, country, image_path):
        """
        Конструктор класу Ball.

        Args:
            name (str): Назва м'яча.
            price (float): Ціна м'яча.
            weight (float): Вага м'яча.
            diameter (float): Діаметр м'яча (см).
            pressure (float): Тиск у м'ячі (атм).
            manufacturer (str): Виробник м'яча.
            material (str): Матеріал м'яча.
            year (str): Рік випуску м'яча.
            country (str): Країна виробництва м'яча.
            image_path (str): Шлях до файлу із зображенням м'яча.
        """
        super().__init__(name, price, weight) # Викликаємо конструктор батьківського класу SportsEquipment,
        # передаючи йому загальні для всього спортивного обладнання атрибути:
        # назву, ціну та вагу.
        self.diameter = diameter  # Діаметр м'яча (атрибут self.diameter).
        self.pressure = pressure  # Тиск у м'ячі (атрибут self.pressure).
        # new values
        self.manufacturer = manufacturer  # Виробник м'яча (атрибут self.manufacturer).
        self.material = material  # Матеріал м'яча (атрибут self.material).
        self.year = year  # Рік випуску м'яча (атрибут self.year).
        self.country = country  # Країна виробництва м'яча (атрибут self.country).
        self.image_path = image_path # Шлях до зображення м'яча (атрибут self.image_path).

    def getInfo(self):
        """
        Метод для отримання інформації про футбольний м'яч у вигляді рядка.

        Returns:
            str: Рядок з інформацією про м'яч, включаючи інформацію від батьківського класу.
        """
        return (f"{super().getInfo()}\n" # Викликаємо метод getInfo() батьківського класу SportsEquipment
                # для отримання базової інформації (назва, ціна, вага).
                f"Діаметр: {self.diameter} см\n"
                f"Тиск: {self.pressure} атм\n"
                f"Виробник: {self.manufacturer}\n"
                f"Матеріал: {self.material}\n"
                f"Рік випуску: {self.year}\n"
                f"Країна: {self.country}\n")
        # f"Зображення: {self.image_path}") # Цей рядок закоментований, тому шлях до зображення не включається
        # у вихідну інформацію.