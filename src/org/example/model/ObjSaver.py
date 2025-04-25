import json # Імпортуємо модуль json з стандартної бібліотеки Python.
# json використовується для роботи з даними у форматі JSON (JavaScript Object Notation).
import os # Імпортуємо модуль os з стандартної бібліотеки Python.
# os надає способи взаємодії з операційною системою, включаючи роботу з файловою системою.

from src.org.example.model.CreateObj import CreateObj # Імпортуємо клас CreateObj, який використовується для
# створення об'єктів Ball при завантаженні даних.


class ObjSaver:
    """
    Клас, що відповідає за збереження та завантаження об'єктів Ball у JSON-файл.
    """
    FILE_PATH = "../../../resource/soccer_balls.json" # Визначаємо константу FILE_PATH, яка вказує шлях до файлу,
    # де будуть зберігатися дані про футбольні м'ячі.

    @staticmethod
    def save(ball_obj):
        """
        Статичний метод для збереження об'єкта Ball у JSON-файл.

        Args:
            ball_obj (Ball): Об'єкт класу Ball, який потрібно зберегти.
        """
        data = { # Створюємо словник data, який представляє об'єкт Ball у форматі JSON.
            "name": ball_obj.name, # Значення атрибута name об'єкта ball_obj.
            "price": ball_obj.price, # Значення атрибута price об'єкта ball_obj.
            "weight": ball_obj.weight, # Значення атрибута weight об'єкта ball_obj.
            "diameter": ball_obj.diameter, # Значення атрибута diameter об'єкта ball_obj.
            "pressure": ball_obj.pressure, # Значення атрибута pressure об'єкта ball_obj.
            "manufacturer": ball_obj.manufacturer, # Значення атрибута manufacturer об'єкта ball_obj.
            "material": ball_obj.material, # Значення атрибута material об'єкта ball_obj.
            "year": ball_obj.year, # Значення атрибута year об'єкта ball_obj.
            "country": ball_obj.country, # Значення атрибута country об'єкта ball_obj.
            "image_path": ball_obj.image_path # Значення атрибута image_path об'єкта ball_obj.
        }

        if not os.path.exists(ObjSaver.FILE_PATH): # Перевіряємо, чи існує файл за шляхом FILE_PATH.
            with open(ObjSaver.FILE_PATH, "w", encoding="utf-8") as file: # Якщо файл не існує, відкриваємо його для запису ('w')
                # з кодуванням UTF-8. Конструкція 'with open(...)'
                # гарантує автоматичне закриття файлу після завершення роботи.
                json.dump([data], file, indent=4, ensure_ascii=False) # Записуємо список, що містить словник data, у файл у форматі JSON
                # з відступами (indent=4) для кращої читабельності та
                # вимкненою екранізацією не-ASCII символів (ensure_ascii=False).
        else: # Якщо файл вже існує.
            with open(ObjSaver.FILE_PATH, "r+", encoding="utf-8") as file: # Відкриваємо файл для читання та запису ('r+') з кодуванням UTF-8.
                try:
                    content = json.load(file) # Намагаємося завантажити вміст файлу як об'єкт JSON (зазвичай список).
                    content.append(data) # Додаємо новий словник data до завантаженого списку.
                    file.seek(0) # Переміщуємо файловий курсор на початок файлу.
                    json.dump(content, file, indent=4, ensure_ascii=False) # Записуємо оновлений список назад у файл, перезаписуючи його вміст.
                except json.JSONDecodeError: # Обробляємо виняток JSONDecodeError, який може виникнути, якщо файл порожній або містить некоректний JSON.
                    json.dump([data], file, indent=4, ensure_ascii=False) # У випадку помилки декодування, записуємо новий список з одним об'єктом.

    @staticmethod
    def load_all():
        """
        Статичний метод для завантаження всіх об'єктів Ball з JSON-файлу.

        Returns:
            list: Список об'єктів класу Ball, завантажених з файлу.
                  Повертає порожній список, якщо файл не існує або містить некоректний JSON.
        """
        if os.path.exists(ObjSaver.FILE_PATH): # Перевіряємо, чи існує файл за шляхом FILE_PATH.
            with open(ObjSaver.FILE_PATH, "r", encoding="utf-8") as file: # Відкриваємо файл для читання ('r') з кодуванням UTF-8.
                try:
                    data_list = json.load(file) # Завантажуємо вміст файлу як об'єкт JSON (очікується список словників).
                    return [CreateObj.create_soccer_ball(**data) for data in data_list] # Використовуємо генератор списку для створення
                    # об'єктів Ball з кожного словника у списку data_list.
                    # Оператор ** розпаковує словник data як іменовані аргументи
                    # для методу CreateObj.create_soccer_ball().
                except json.JSONDecodeError: # Обробляємо виняток JSONDecodeError, якщо файл містить некоректний JSON.
                    return [] # Повертаємо порожній список у випадку помилки.
        else: # Якщо файл не існує.
            return [] # Повертаємо порожній список.

    @staticmethod
    def delete(ball_name):
        """
        Статичний метод для видалення об'єкта Ball з JSON-файлу за його назвою.

        Args:
            ball_name (str): Назва об'єкта Ball, який потрібно видалити.
        """
        if os.path.exists(ObjSaver.FILE_PATH):
            with open(ObjSaver.FILE_PATH, "r+", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                    updated_content = [item for item in content if item["name"] != ball_name]
                    file.seek(0)
                    file.truncate() # Очищаємо вміст файлу перед записом оновлених даних
                    json.dump(updated_content, file, indent=4, ensure_ascii=False)
                    return True # Повертаємо True, якщо об'єкт був знайдений і видалений
                except json.JSONDecodeError:
                    return False # Повертаємо False, якщо файл порожній або містить некоректний JSON
        else:
            return False # Повертаємо False, якщо файл не існує