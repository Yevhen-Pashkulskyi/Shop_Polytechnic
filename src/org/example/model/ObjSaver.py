import csv # Імпортує модуль csv для роботи з файлами CSV (Comma Separated Values).
import json # Імпортує модуль json для роботи з файлами JSON (JavaScript Object Notation).
import os # Імпортує модуль os для роботи з операційною системою, наприклад, для створення директорій та перевірки існування файлів.
import pickle # Імпортує модуль pickle для серіалізації та десеріалізації об'єктів Python (перетворення об'єктів у потік байтів та навпаки).
from tkinter import messagebox # Імпортує модуль messagebox з tkinter для виведення вікон повідомлень (помилки, інформаційні повідомлення).
from src.org.example.model.CreateObj import CreateObj # Імпортує клас CreateObj з модуля CreateObj.py, який, ймовірно, використовується для створення об'єктів футбольних м'ячів.

class ObjSaver:
    """
    Клас ObjSaver відповідає за збереження та завантаження даних про футбольні м'ячі у різних форматах файлів.
    Він забезпечує абстракцію від формату файлу, дозволяючи зберігати та завантажувати дані без явного вказання формату у коді,
    який використовує цей клас.
    """

    BASE_DIR = "../../../resource/Pashkulskyi" # Базова директорія для збереження файлів даних.  Ця директорія знаходиться на три рівні вище поточного файлу, в директорії resource/Pashkulskyi.
    NAME_FILE = "soccer_balls" # Назва файлу без розширення.  Використовується для створення імен файлів у різних форматах.
    JSON_FILE = os.path.join(BASE_DIR, NAME_FILE + ".json") # Повний шлях до файлу JSON.
    TXT_FILE = os.path.join(BASE_DIR, NAME_FILE + ".txt") # Повний шлях до файлу TXT.
    CSV_FILE = os.path.join(BASE_DIR, NAME_FILE + ".csv") # Повний шлях до файлу CSV.
    BIN_FILE = os.path.join(BASE_DIR, NAME_FILE + ".bin") # Повний шлях до бінарного файлу (pickle).

    @staticmethod
    def ensure_directory():
        """
        Перевіряє, чи існує директорія для збереження файлів даних. Якщо директорія не існує, вона створюється.
        Цей метод викликається перед кожною операцією збереження або завантаження, щоб гарантувати, що директорія існує.
        """
        if not os.path.exists(ObjSaver.BASE_DIR): # Перевіряє, чи існує директорія ObjSaver.BASE_DIR.
            os.makedirs(ObjSaver.BASE_DIR) # Якщо директорія не існує, створює її.

    @staticmethod
    def save(ball_obj):
        """
        Зберігає інформацію про футбольний м'яч у різних форматах файлів (JSON, TXT, CSV, BIN).

        Args:
            ball_obj (CreateObj): Об'єкт CreateObj, що представляє футбольний м'яч.  Він містить атрибути, такі як name, price, weight і т.д.
        """
        ObjSaver.ensure_directory() # Переконується, що директорія для збереження файлів існує.
        # Створює словник data, що містить інформацію про м'яч.  Цей словник буде записаний у файли.
        data = {
            "name": ball_obj.name,
            "price": ball_obj.price,
            "weight": ball_obj.weight,
            "diameter": ball_obj.diameter,
            "pressure": ball_obj.pressure,
            "manufacturer": ball_obj.manufacturer,
            "material": ball_obj.material,
            "year": ball_obj.year,
            "country": ball_obj.country,
            "image_path": ball_obj.image_path
        }

        # Збереження в JSON
        if not os.path.exists(ObjSaver.JSON_FILE): # Перевіряє, чи існує файл JSON.
            with open(ObjSaver.JSON_FILE, "w", encoding="utf-8") as file: # Відкриває файл JSON для запису.  Використовується кодування utf-8 для підтримки Unicode.
                json.dump([data], file, indent=4, ensure_ascii=False) # Записує список, що містить словник data, у файл JSON з відступами для читабельності та без екранування символів Unicode.
        else:
            with open(ObjSaver.JSON_FILE, "r+", encoding="utf-8") as file: # Відкриває файл JSON для читання та запису.
                try:
                    content = json.load(file) # Зчитує поточний вміст файлу JSON.
                    content.append(data) # Додає новий словник data до зчитаного вмісту.
                    file.seek(0) # Переміщує вказівник файлу на початок файлу.
                    json.dump(content, file, indent=4, ensure_ascii=False) # Записує оновлений вміст у файл JSON.
                except json.JSONDecodeError: # Обробляє випадок, коли файл JSON порожній або містить некоректний JSON.
                    json.dump([data], file, indent=4, ensure_ascii=False) # Записує список, що містить словник data, у файл JSON.

        # Збереження в TXT
        with open(ObjSaver.TXT_FILE, "a", encoding="utf-8") as file: # Відкриває файл TXT для додавання даних.
            # Записує інформацію про м'яч у форматі "ключ: значення" у файл TXT.
            file.write(
                f"Name: {data['name']}, Price: {data['price']}, Weight: {data['weight']}, "
                f"Diameter: {data['diameter']}, Pressure: {data['pressure']}, "
                f"Manufacturer: {data['manufacturer']}, Material: {data['material']}, "
                f"Year: {data['year']}, Country: {data['country']}, Image_path: {data['image_path']}\n"
            )

        # Збереження в CSV
        csv_headers = ["name", "price", "weight", "diameter", "pressure", "manufacturer", "material", "year", "country",
                       "image_path"] # Заголовки для файлу CSV.
        file_exists = os.path.exists(ObjSaver.CSV_FILE) # Перевіряє, чи існує файл CSV.
        with open(ObjSaver.CSV_FILE, "a", encoding="utf-8", newline='') as file: # Відкриває файл CSV для додавання даних.
            writer = csv.DictWriter(file, fieldnames=csv_headers) # Створює об'єкт csv.DictWriter для запису словників у форматі CSV.
            if not file_exists: # Якщо файл не існує, записує заголовки.
                writer.writeheader()
            writer.writerow(data) # Записує словник data як рядок у файл CSV.

        # Збереження в BIN (pickle)
        balls = ObjSaver.load_all(source="bin")  # Завантажує існуючі об'єкти м'ячів з файлу BIN.
        balls.append(ball_obj) # Додає новий об'єкт м'яча до списку.
        with open(ObjSaver.BIN_FILE, "wb") as file: # Відкриває файл BIN для запису в двійковому режимі.
            pickle.dump(balls, file) # Серіалізує список об'єктів balls та записує його у файл.

    @staticmethod
    def load_all(source="json"):
        """
        Завантажує інформацію про футбольні м'ячі з файлу вказаного формату.

        Args:
            source (str): Формат файлу для завантаження даних ("json", "txt", "csv" або "bin"). За замовчуванням "json".

        Returns:
            list: Список об'єктів CreateObj, що представляють футбольні м'ячі.
        """
        ObjSaver.ensure_directory() # Переконується, що директорія для файлів даних існує.
        balls = [] # Ініціалізує порожній список для зберігання об'єктів м'ячів.

        if source == "json" and os.path.exists(ObjSaver.JSON_FILE): # Якщо джерело - JSON та файл існує.
            with open(ObjSaver.JSON_FILE, "r", encoding="utf-8") as file: # Відкриває файл JSON для читання.
                try:
                    data_list = json.load(file) # Зчитує дані з файлу JSON.
                    balls = [CreateObj.create_soccer_ball(**data) for data in data_list] # Створює список об'єктів CreateObj зі зчитаних даних.
                except json.JSONDecodeError: # Обробляє помилку декодування JSON (наприклад, якщо файл порожній або пошкоджений).
                    messagebox.showerror("Помилка", "Не вдалося прочитати JSON файл") # Виводить повідомлення про помилку.
                    balls = [] # Повертає порожній список у випадку помилки.

        elif source == "txt" and os.path.exists(ObjSaver.TXT_FILE): # Якщо джерело - TXT та файл існує.
            with open(ObjSaver.TXT_FILE, "r", encoding="utf-8") as file: # Відкриває файл TXT для читання.
                for line in file: # Зчитує кожен рядок з файлу.
                    try:
                        parts = line.strip().split(", ") # Розбиває рядок на частини за допомогою коми та пробілу.
                        data = {} # Ініціалізує порожній словник для зберігання даних про м'яч з поточного рядка.
                        for part in parts:
                            key, value = part.split(": ", 1) # Розбиває кожну частину на ключ та значення.
                            data[key.lower().replace(" ", "_")] = value # Перетворює ключ у нижній регістр та замінює пробіли на підкреслення.
                        balls.append(CreateObj.create_soccer_ball(**data)) # Створює об'єкт CreateObj зі словника даних та додає його до списку.
                    except Exception: # Обробляє можливі помилки при обробці рядка (наприклад, неправильний формат рядка).
                        continue # Пропускає поточний рядок, якщо виникла помилка.

        elif source == "csv" and os.path.exists(ObjSaver.CSV_FILE): # Якщо джерело - CSV та файл існує.
            with open(ObjSaver.CSV_FILE, "r", encoding="utf-8") as file: # Відкриває файл CSV для читання.
                reader = csv.DictReader(file) # Створює об'єкт csv.DictReader для читання даних з файлу CSV у вигляді словників.
                for row in reader: # Зчитує кожен рядок з файлу CSV у вигляді словника.
                    balls.append(CreateObj.create_soccer_ball(**row)) # Створює об'єкт CreateObj зі словника та додає його до списку.

        elif source == "bin" and os.path.exists(ObjSaver.BIN_FILE): # Якщо джерело - BIN та файл існує.
            with open(ObjSaver.BIN_FILE, "rb") as file: # Відкриває файл BIN для читання в двійковому режимі.
                try:
                    balls = pickle.load(file) # Десеріалізує дані з файлу та завантажує їх у список balls.
                except Exception: # Обробляє можливі помилки при десеріалізації (наприклад, файл пошкоджений або містить некоректні дані).
                    messagebox.showerror("Помилка", "Не вдалося прочитати BIN файл") # Виводить повідомлення про помилку.
                    balls = [] # Присвоює balls порожній список.

        return balls # Повертає список об'єктів CreateObj.

    @staticmethod
    def delete(ball_name):
        """
        Видаляє інформацію про футбольний м'яч з усіх форматів файлів за назвою м'яча.

        Args:
            ball_name (str): Назва м'яча, який потрібно видалити.

        Returns:
            bool: True, якщо видалення пройшло успішно, False - якщо виникли помилки.
        """
        ObjSaver.ensure_directory() # Переконується, що директорія існує.
        success = False # Ініціалізує змінну success значенням False.

        # Видалення з JSON
        if os.path.exists(ObjSaver.JSON_FILE): # Перевіряє, чи існує файл JSON.
            with open(ObjSaver.JSON_FILE, "r+", encoding="utf-8") as file: # Відкриває файл JSON для читання та запису.
                try:
                    content = json.load(file) # Зчитує вміст файлу JSON.
                    updated_content = [item for item in content if item["name"] != ball_name] # Фільтрує список, залишаючи лише ті елементи, назва яких не збігається з ball_name.
                    file.seek(0) # Переміщує вказівник на початок файлу.
                    file.truncate() # Обрізає файл до поточного положення вказівника (тобто, видаляє все).
                    json.dump(updated_content, file, indent=4, ensure_ascii=False) # Записує відфільтрований список у файл.
                    success = True # Встановлює success в True, якщо операція пройшла успішно.
                except json.JSONDecodeError: # Обробляє помилку декодування JSON.
                    success = False # Встановлює success в False, якщо виникла помилка.

        # Видалення з TXT
        if os.path.exists(ObjSaver.TXT_FILE): # Перевіряє, чи існує файл TXT.
            with open(ObjSaver.TXT_FILE, "r", encoding="utf-8") as file: # Відкриває файл TXT для читання.
                lines = file.readlines() # Зчитує всі рядки з файлу.
            with open(ObjSaver.TXT_FILE, "w", encoding="utf-8") as file: # Відкриває файл TXT для запису.
                for line in lines: # Перебирає всі рядки.
                    if f"Name: {ball_name}" not in line: # Якщо рядок не містить інформацію про м'яч з заданою назвою,
                        file.write(line) # записує його у файл.
                success = True # Встановлює success в True.

        # Видалення з CSV
        if os.path.exists(ObjSaver.CSV_FILE): # Перевіряє, чи існує файл CSV.
            with open(ObjSaver.CSV_FILE, "r", encoding="utf-8") as file: # Відкриває файл CSV для читання.
                reader = csv.DictReader(file) # Створює об'єкт csv.DictReader.
                rows = [row for row in reader if row["name"] != ball_name] # Фільтрує рядки, залишаючи лише ті, назва яких не збігається з ball_name.
            with open(ObjSaver.CSV_FILE, "w", encoding="utf-8", newline='') as file: # Відкриває файл CSV для запису.
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames) # Створює об'єкт csv.DictWriter з тими ж заголовками, що й у зчитаному файлі.
                writer.writeheader() # Записує заголовки у файл.
                writer.writerows(rows) # Записує відфільтровані рядки у файл.
                success = True # Встановлює success в True.

        # Видалення з BIN
        if os.path.exists(ObjSaver.BIN_FILE): # Перевіряє, чи існує файл BIN.
            balls = ObjSaver.load_all() # Завантажує всі об'єкти м'ячів з файлу BIN.
            balls = [ball for ball in balls if ball.name != ball_name] # Фільтрує список, залишаючи лише ті об'єкти, назва яких не збігається з ball_name.
            with open(ObjSaver.BIN_FILE, "wb") as file: # Відкриває файл BIN для запису в двійковому режимі.
                pickle.dump(balls, file) # Серіалізує відфільтрований список та записує його у файл.
                success = True # Встановлює success в True.

        return success # Повертає значення змінної success, що вказує на успішність операції.
