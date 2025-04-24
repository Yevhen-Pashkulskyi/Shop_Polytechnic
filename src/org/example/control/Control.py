from tkinter import messagebox # Імпортуємо модуль messagebox з бібліотеки tkinter.
# messagebox використовується для відображення стандартних діалогових вікон,
# таких як повідомлення про помилки, попередження тощо.

from src.org.example.model.CreateObj import CreateObj # Імпортуємо клас CreateObj з вказаного модуля.
# CreateObj, ймовірно, містить статичні методи для створення
# об'єктів різних сутностей (у цьому випадку - футбольних м'ячів).
from src.org.example.model.ObjSaver import ObjectSaver # Імпортуємо клас ObjectSaver з вказаного модуля.
# ObjectSaver відповідає за збереження даних об'єктів у файл.


class Control:
    def __init__(self, gui):
        """
        Конструктор класу Control.

        Args:
            gui (GUIBuilder): Екземпляр класу GUIBuilder, що надає доступ до елементів графічного інтерфейсу.
        """
        self.gui = gui # Зберігаємо посилання на об'єкт GUIBuilder (gui) в атрибуті self.gui.
        # Це дозволяє класу Control взаємодіяти з елементами GUI, такими як поля введення,
        # мітки для виведення результатів тощо.

    def create_soccer_ball(self):
        """
        Метод для створення об'єкта футбольного м'яча на основі даних з GUI.
        Викликається при натисканні кнопки "✅ Створити об'єкт".
        """
        try:
            name = self.gui.name_entry.get().strip() # Отримуємо значення з поля введення назви (self.gui.name_entry),
            # видаляємо зайві пробіли на початку та в кінці за допомогою .strip().
            # self.gui.name_entry - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.Entry для введення назви.
            if not name:
                raise ValueError("⛔ Поле «Назва» не може бути порожнім.") # Якщо поле назви порожнє,
                # генеруємо виняток ValueError з відповідним повідомленням.

            price = self.get_float(self.gui.price_entry, "Ціна (грн)") # Викликаємо метод self.get_float() для отримання
            # значення ціни з поля введення (self.gui.price_entry)
            # та його валідації.
            # self.gui.price_entry - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.Entry для введення ціни.
            weight = self.get_float(self.gui.weight_entry, "Вага (кг)") # Аналогічно для ваги (self.gui.weight_entry).
            # self.gui.weight_entry - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.Entry для введення ваги.
            diameter = self.get_float(self.gui.diameter_entry, "Діаметр (см)") # Аналогічно для діаметра (self.gui.diameter_entry).
            # self.gui.diameter_entry - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.Entry для введення діаметра.
            pressure = self.get_float(self.gui.pressure_entry, "Тиск (атм)") # Аналогічно для тиску (self.gui.pressure_entry).
            # self.gui.pressure_entry - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.Entry для введення тиску.

            # Получаем выбранного производителя
            if self.gui.manufacturer_listbox.size() == 0: # Перевіряємо, чи список виробників (self.gui.manufacturer_listbox) не порожній.
                # self.gui.manufacturer_listbox - це атрибут об'єкта GUIBuilder,
                # який є об'єктом tkinter.Listbox для вибору виробника.
                raise ValueError("⚠️ Список виробників не може бути порожнім.")

            manufacturer = self.get_selected_listbox_value(self.gui.manufacturer_listbox, "виробника") # Отримуємо вибраного виробника
            # зі списку (self.gui.manufacturer_listbox).
            material = self.gui.selected_material.get() # Отримуємо вибраний матеріал з OptionMenu (self.gui.selected_material).
            # self.gui.selected_material - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.StringVar, що зберігає вибраний матеріал.
            year = self.gui.selected_year.get() # Отримуємо вибраний рік випуску з OptionMenu (self.gui.selected_year).
            # self.gui.selected_year - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.StringVar, що зберігає вибраний рік.
            country = self.gui.selected_country.get() # Отримуємо вибрану країну виробництва з OptionMenu (self.gui.selected_country).
            # self.gui.selected_country - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.StringVar, що зберігає вибрану країну.
            image_path = self.gui.view.get_current_image_path() # Отримуємо шлях до поточного зображення з галереї (self.gui.view).
            # self.gui.view - це атрибут об'єкта GUIBuilder,
            # який є об'єктом GalleryView.

            ball = CreateObj.create_soccer_ball(name, price, weight, diameter, pressure, # Викликаємо статичний метод create_soccer_ball
                                                manufacturer, material, year, country,   # класу CreateObj для створення об'єкта Ball.
                                                image_path)

            ObjectSaver.save(ball) # Викликаємо статичний метод save класу ObjectSaver для збереження створеного об'єкта ball.

            self.gui.result_label.config(text=ball.getInfo()) # Оновлюємо текст мітки результату (self.gui.result_label)
            # інформацією про створений м'яч, отриманою за допомогою методу ball.getInfo().
            # self.gui.result_label - це атрибут об'єкта GUIBuilder,
            # який є об'єктом tkinter.Label для відображення результату.
            self.gui.update_result_image(image_path) # Оновлюємо відображення зображення результату, викликаючи метод
            # self.gui.update_result_image() та передаючи йому шлях до зображення.

        except ValueError as ve: # Обробляємо винятки ValueError, які можуть виникнути при валідації введених даних.
            messagebox.showerror("Помилка валідації", str(ve)) # Відображаємо діалогове вікно з повідомленням про помилку валідації.
        except Exception as e: # Обробляємо будь-які інші винятки, які можуть виникнути під час виконання.
            messagebox.showerror("Помилка", f"⚠️ Сталася непередбачена помилка:\n{e}") # Відображаємо діалогове вікно з повідомленням про непередбачену помилку.

    def get_selected_listbox_value(self, listbox, label):
        """
        Метод для отримання вибраного значення зі списку (tkinter.Listbox).

        Args:
            listbox (tkinter.Listbox): Список, з якого потрібно отримати вибране значення.
            label (str): Текстове представлення типу значення (наприклад, "виробника") для повідомлення про помилку.

        Returns:
            str: Вибране значення зі списку.

        Raises:
            ValueError: Якщо жодне значення не вибрано у списку.
        """
        try:
            index = listbox.curselection()[0] # Отримуємо індекс вибраного елемента в списку.
            # Метод curselection() повертає кортеж з індексами вибраних елементів.
            # Ми беремо перший (і єдиний, оскільки дозволено лише одне виділення).
            return listbox.get(index) # Повертаємо значення елемента за отриманим індексом.
        except IndexError: # Обробляємо виняток IndexError, який виникає, якщо жоден елемент не вибрано.
            raise ValueError(f"⛔ Оберіть значення {label} зі списку.") # Генеруємо ValueError з повідомленням про необхідність вибору.

    # функция для проверки ввода на число и отрецательное число
    def get_float(self, entry, label_name):
        """
        Метод для отримання значення з поля введення (tkinter.Entry), перетворення його на float та валідації.

        Args:
            entry (tkinter.Entry): Поле введення, з якого потрібно отримати значення.
            label_name (str): Назва поля для повідомлень про помилки.

        Returns:
            float: Значення, введене в поле, у вигляді числа з плаваючою комою.

        Raises:
            ValueError: Якщо поле порожнє, містить не числове значення або від'ємне число.
        """
        value = entry.get().strip() # Отримуємо значення з поля введення та видаляємо зайві пробіли.
        if not value:
            raise ValueError(f"⛔ Поле «{label_name}» не може бути порожнім.") # Якщо поле порожнє, генеруємо ValueError.
        try:
            float_value = float(value) # Намагаємося перетворити отримане значення на float.
        except ValueError: # Обробляємо ValueError, який виникає, якщо значення не може бути перетворено на float.
            raise ValueError(f"⛔ Поле «{label_name}» повинно містити число.")
        if float_value <= 0: # Перевіряємо, чи отримане число не є від'ємним або нулем.
            raise ValueError(f"⛔ Значення «{label_name}» не може бути від'ємним.")
        return float_value # Повертаємо отримане та валідоване значення float.