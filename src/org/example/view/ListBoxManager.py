from tkinter import END, messagebox # Імпортуємо константу END та модуль messagebox з бібліотеки tkinter.
# END використовується для вставки елементів у кінець списку.
# messagebox використовується для відображення діалогових вікон.


class ListboxManager:
    """
    Клас, що містить статичні методи для керування елементами віджета tkinter.Listbox.
    """
    @staticmethod
    def add_item(listbox, entry_widget, limit=6):
        """
        Статичний метод для додавання нового елемента до списку (tkinter.Listbox).

        Args:
            listbox (tkinter.Listbox): Список, до якого потрібно додати елемент.
            entry_widget (tkinter.Entry): Поле введення, з якого отримується текст для нового елемента.
            limit (int, optional): Максимальна кількість елементів у списку. За замовчуванням - 6.
        """
        if listbox.size() >= limit: # Перевіряємо, чи не перевищено ліміт елементів у списку.
            messagebox.showwarning("Ліміт", f"⚠️ Максимальна кількість виробників — {limit}") # Відображаємо попередження, якщо ліміт досягнуто.
            return # Виходимо з функції, не додаючи елемент.
        item = entry_widget.get().strip() # Отримуємо текст з поля введення та видаляємо зайві пробіли.
        if item: # Перевіряємо, чи текст не порожній.
            listbox.insert(END, item) # Додаємо текст до кінця списку.
            entry_widget.delete(0, END) # Очищаємо поле введення після додавання.

    @staticmethod
    def edit_item(listbox, entry_widget):
        """
        Статичний метод для редагування вибраного елемента у списку (tkinter.Listbox).

        Args:
            listbox (tkinter.Listbox): Список, в якому потрібно відредагувати елемент.
            entry_widget (tkinter.Entry): Поле введення, з якого отримується новий текст для елемента.
        """
        try:
            index = listbox.curselection()[0] # Отримуємо індекс вибраного елемента.
            new_value = entry_widget.get().strip() # Отримуємо новий текст з поля введення.
            if new_value: # Перевіряємо, чи новий текст не порожній.
                listbox.delete(index) # Видаляємо старий елемент за індексом.
                listbox.insert(index, new_value) # Вставляємо новий текст на місце старого елемента.
                entry_widget.delete(0, END) # Очищаємо поле введення.
        except IndexError: # Обробляємо виняток, якщо жоден елемент не вибрано.
            messagebox.showwarning("⚠️", "Оберіть виробника для редагування.")

    @staticmethod
    def delete_item(listbox):
        """
        Статичний метод для видалення вибраного елемента зі списку (tkinter.Listbox).

        Args:
            listbox (tkinter.Listbox): Список, з якого потрібно видалити елемент.
        """
        try:
            index = listbox.curselection()[0] # Отримуємо індекс вибраного елемента.
            listbox.delete(index) # Видаляємо елемент за індексом.
        except IndexError: # Обробляємо виняток, якщо жоден елемент не вибрано.
            messagebox.showwarning("⚠️", "Оберіть виробника для видалення.")

    @staticmethod
    def sort_items(listbox):
        """
        Статичний метод для сортування елементів у списку (tkinter.Listbox) за алфавітом.

        Args:
            listbox (tkinter.Listbox): Список, який потрібно відсортувати.
        """
        items = list(listbox.get(0, END)) # Отримуємо всі елементи списку у вигляді звичайного списку Python.
        items.sort() # Сортуємо отриманий список.
        listbox.delete(0, END) # Очищаємо вміст списку Listbox.
        for item in items: # Додаємо відсортовані елементи назад до Listbox.
            listbox.insert(END, item)

    @staticmethod
    def reverse_items(listbox):
        """
        Статичний метод для зміни порядку елементів у списку (tkinter.Listbox) на зворотний.

        Args:
            listbox (tkinter.Listbox): Список, порядок елементів якого потрібно змінити.
        """
        items = list(listbox.get(0, END)) # Отримуємо всі елементи списку.
        items.reverse() # Змінюємо порядок елементів у списку на зворотний.
        listbox.delete(0, END) # Очищаємо Listbox.
        for item in items: # Додаємо елементи у зворотному порядку назад до Listbox.
            listbox.insert(END, item)