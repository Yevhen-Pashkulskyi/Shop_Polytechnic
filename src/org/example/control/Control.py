from src.org.example.model.ObjSaver import ObjSaver # Імпортуємо клас ObjSaver з модуля ObjSaver.py, який відповідає за збереження та завантаження об'єктів.
from src.org.example.model.CreateObj import CreateObj # Імпортуємо клас CreateObj з модуля CreateObj.py, який відповідає за створення об'єктів.
from src.org.example.view.GUIBuilder import GUIBuilder # Імпортуємо клас GUIBuilder з модуля GUIBuilder.py, який відповідає за побудову графічного інтерфейсу.
from src.org.example.view.GalleryView import GalleryView # Імпортуємо клас GalleryView з модуля GalleryView.py, який відповідає за відображення галереї зображень.

class Control:
    """
    Клас Control відповідає за управління логікою програми.
    Він координує взаємодію між моделлю (даними) та представленням (GUI).
    """
    def __init__(self):
        """
        Ініціалізує об'єкт Control.
        Встановлює початкові значення для атрибутів gui, gallery, loaded_objects та current_loaded_index.
        """
        self.gui = None # Змінна для зберігання об'єкта GUIBuilder (інтерфейс).
        self.gallery = None # Змінна для зберігання об'єкта GalleryView (галерея зображень).
        self.loaded_objects = [] # Список для зберігання завантажених об'єктів (наприклад, футбольних м'ячів).
        self.current_loaded_index = 0 # Індекс поточного завантаженого об'єкта у списку loaded_objects.

    def init_gui(self, root):
        """
        Ініціалізує графічний інтерфейс (GUI) та завантажує об'єкти.

        Args:
            root (tkinter.Tk): Кореневий об'єкт Tkinter для створення GUI.
        """
        self.gui = GUIBuilder(root, self) # Створює об'єкт GUIBuilder, передаючи кореневий об'єкт Tkinter та посилання на поточний об'єкт Control.
        self.gallery = GalleryView(self.gui.input_tab) # Створює об'єкт GalleryView, передаючи вкладку введення даних з GUIBuilder.
        self.gui.set_gallery_view(self.gallery) # Встановлює об'єкт GalleryView для GUIBuilder, щоб вони могли взаємодіяти.
        self.gallery.show_image_ball() # Показує початкове зображення м'яча в галереї.
        self.load_objects() # Завантажує об'єкти з обраного джерела (за замовчуванням з JSON).

    def create_soccer_ball(self):
        """
        Створює об'єкт футбольного м'яча на основі даних, введених користувачем, та зберігає його.
        Також оновлює GUI для відображення створеного об'єкта.
        """
        try:
            name = self.gui.name_entry.get().strip() # Отримує назву м'яча з поля введення та видаляє зайві пробіли.
            if not name: # Перевіряє, чи введено назву.
                raise ValueError("⛔ Поле «Назва» не може бути порожнім.") # Викликає виняток, якщо назва не введена.

            price = self.get_float(self.gui.price_entry, "Ціна (грн)") # Отримує та валідує ціну м'яча.
            weight = self.get_float(self.gui.weight_entry, "Вага (кг)") # Отримує та валідує вагу м'яча.
            diameter = self.get_float(self.gui.diameter_entry, "Діаметр (см)") # Отримує та валідує діаметр м'яча.
            pressure = self.get_float(self.gui.pressure_entry, "Тиск (атм)") # Отримує та валідує тиск м'яча.

            manufacturer = self.get_selected_listbox_value(self.gui.manufacturer_listbox, "виробника") # Отримує обраного виробника зі списку.
            material = self.gui.selected_material.get() # Отримує обраний матеріал м'яча.
            year = self.gui.selected_year.get() # Отримує обраний рік випуску м'яча.
            country = self.gui.selected_country.get() # Отримує обрану країну виробництва м'яча.
            image_path = self.gallery.get_current_image_path() # Отримує шлях до зображення м'яча з галереї.

            ball = CreateObj.create_soccer_ball(name, price, weight, diameter, pressure, manufacturer, material, year,
                country, image_path) # Створює об'єкт футбольного м'яча за допомогою CreateObj.

            ObjSaver.save(ball) # Зберігає створений об'єкт у файл.
            self.gui.result_label.config(text=ball.getInfo()) # Оновлює текстову мітку в GUI інформацією про створений м'яч.
            self.gui.update_result_image(image_path) # Оновлює відображення зображення в GUI.
            self.load_objects() # Перезавантажує список об'єктів для оновлення відображення.

        except ValueError as ve: # Обробляє помилки валідації даних.
            from tkinter import messagebox # Імпортує модуль messagebox для відображення вікон повідомлень.
            messagebox.showerror("Помилка валідації", str(ve)) # Показує вікно з помилкою валідації.
        except Exception as e: # Обробляє інші можливі помилки.
            from tkinter import messagebox # Імпортує модуль messagebox для відображення вікон повідомлень.
            messagebox.showerror("Помилка", f"⚠️ Сталася помилка: {e}") # Показує вікно з загальною помилкою.

    def load_objects(self, source="json"):
        """
        Завантажує об'єкти з вказаного джерела.

        Args:
            source (str): Джерело даних для завантаження об'єктів ("json", "txt", "csv" або "bin"). За замовчуванням "json".
        """
        self.loaded_objects = ObjSaver.load_all(source=source) # Завантажує об'єкти з вказаного джерела.
        self.gui.update_data_source(source.upper()) # Оновлює мітку в GUI з назвою поточного джерела даних.
        if self.loaded_objects: # Перевіряє, чи є завантажені об'єкти.
            self.show_object(0) # Якщо є, відображає перший об'єкт.
        else:
            self.gui.result_label.config(text="Об'єкти відсутні") # Якщо немає об'єктів, виводить повідомлення.
            self.gui.result_image_label.config(image='', text="❌") # Очищає поле для відображення зображення та виводить символ "X".

    def load_objects_from_source(self, source):
        """
        Завантажує об'єкти з обраного джерела. Цей метод викликається при зміні джерела даних у GUI.

        Args:
            source (str): Назва джерела даних ("JSON", "TXT", "CSV" або "BIN").
        """
        self.load_objects(source=source.lower()) # Передає назву джерела в нижньому регістрі в метод load_objects.

    def show_object(self, index):
        """
        Відображає об'єкт з вказаним індексом у GUI.

        Args:
            index (int): Індекс об'єкта для відображення.
        """
        if 0 <= index < len(self.loaded_objects): # Перевіряє, чи індекс знаходиться в межах списку об'єктів.
            ball = self.loaded_objects[index] # Отримує об'єкт за індексом.
            self.gui.result_label.config(text=ball.getInfo()) # Оновлює текстову мітку в GUI інформацією про об'єкт.
            self.gui.update_result_image(ball.image_path) # Оновлює зображення об'єкта в GUI.
            self.current_loaded_index = index # Зберігає поточний індекс об'єкта.

    def show_next_loaded_object(self):
        """
        Відображає наступний об'єкт у списку завантажених об'єктів.
        Якщо досягнуто кінця списку, починає з початку.
        """
        if self.loaded_objects: # Перевіряє, чи є завантажені об'єкти.
            self.current_loaded_index = (self.current_loaded_index + 1) % len(self.loaded_objects) # Обчислює індекс наступного об'єкта за допомогою оператора модуля.
            self.show_object(self.current_loaded_index) # Відображає об'єкт з обчисленим індексом.

    def show_previous_loaded_object(self):
        """
        Відображає попередній об'єкт у списку завантажених об'єктів.
        Якщо досягнуто початку списку, починає з кінця.
        """
        if self.loaded_objects: # Перевіряє, чи є завантажені об'єкти.
            self.current_loaded_index = (self.current_loaded_index - 1) % len(self.loaded_objects) # Обчислює індекс попереднього об'єкта за допомогою оператора модуля.
            self.show_object(self.current_loaded_index) # Відображає об'єкт з обчисленим індексом.

    def delete_current_object(self):
        """
        Видаляє поточний об'єкт зі списку завантажених об'єктів та відповідного файлу.
        Виводить підтвердження перед видаленням.
        """
        if not self.loaded_objects: # Якщо список об'єктів порожній, виходимо з функції.
            return

        from tkinter import messagebox # Імпортуємо модуль messagebox для виведення вікон повідомлень.
        ball = self.loaded_objects[self.current_loaded_index] # Отримуємо поточний об'єкт.
        confirm = messagebox.askyesno("Підтвердження", f"Ви впевнені, що хочете видалити '{ball.name}'?") # Виводимо вікно підтвердження.
        if confirm: # Якщо користувач підтверджує видалення.
            if ObjSaver.delete(ball.name): # Видаляємо об'єкт за допомогою ObjSaver.delete().
                messagebox.showinfo("Успішно", f"Об'єкт '{ball.name}' видалено") # Виводимо повідомлення про успішне видалення.
                self.load_objects() # Перезавантажуємо список об'єктів для оновлення відображення.
            else:
                messagebox.showerror("Помилка", f"Не вдалося видалити '{ball.name}'") # Виводимо повідомлення про помилку, якщо не вдалося видалити об'єкт.

    def get_selected_listbox_value(self, listbox, label):
        """
        Отримує значення, вибране в Listbox.

        Args:
            listbox (tk.Listbox): Об'єкт Listbox.
            label (str): Назва поля, яке відображається користувачеві (для повідомлення про помилку).

        Returns:
            str: Значення, вибране в Listbox.

        Raises:
            ValueError: Якщо не вибрано жодного елемента.
        """
        try:
            index = listbox.curselection()[0] # Отримуємо індекс вибраного елемента.
            return listbox.get(index) # Повертаємо значення елемента.
        except IndexError: # Якщо не вибрано жодного елемента, виникає помилка IndexError.
            raise ValueError(f"⛔ Оберіть значення {label} зі списку.") # Викликаємо виняток ValueError з відповідним повідомленням.

    def get_float(self, entry, label_name):
        """
        Отримує значення з поля вводу та перетворює його у float.

        Args:
            entry (tk.Entry): Об'єкт Entry.
            label_name (str): Назва поля, яке відображається користувачеві (для повідомлення про помилку).

        Returns:
            float: Значення, введене користувачем.

        Raises:
            ValueError: Якщо поле порожнє або введене значення не є числом.
        """
        value = entry.get().strip() # Отримуємо значення з поля вводу та видаляємо зайві пробіли.
        if not value: # Перевіряємо, чи введено значення.
            raise ValueError(f"⛔ Поле «{label_name}» не може бути порожнім.") # Викликаємо виняток ValueError, якщо поле порожнє.
        try:
            float_value = float(value) # Намагаємося перетворити введене значення у float.
        except ValueError: # Якщо введене значення не є числом, виникає помилка ValueError.
            raise ValueError(f"⛔ Поле «{label_name}» повинно містити число.") # Викликаємо виняток ValueError з відповідним повідомленням.
        if float_value <= 0: # Перевіряємо, чи є число додатним.
            raise ValueError(f"⛔ Значення «{label_name}» не може бути від'ємним.") # Викликаємо ValueError, якщо число не додатне.
        return float_value # Повертаємо перетворене число.
