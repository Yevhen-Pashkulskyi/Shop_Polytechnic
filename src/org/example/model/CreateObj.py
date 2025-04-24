from src.org.example.entity.Ball import Ball # Імпортуємо клас Ball з вказаного модуля.
# Ball - клас, що представляє футбольний м'яч.


class CreateObj:
    """
    Клас, що містить статичні методи для створення об'єктів різних сутностей.
    Наразі містить метод лише для створення футбольних м'ячів.
    """
    @staticmethod
    def create_soccer_ball(name, price, weight, diameter, pressure,
                           manufacturer, material, year, country, image_path):
        """
        Статичний метод для створення об'єкта футбольного м'яча (Ball).

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

        Returns:
            Ball: Створений об'єкт класу Ball з переданими атрибутами.
        """
        return Ball(name, price, weight, diameter, pressure, # Створюємо та повертаємо новий екземпляр класу Ball,
                    manufacturer, material, year, country, image_path) # передаючи йому всі необхідні аргументи.