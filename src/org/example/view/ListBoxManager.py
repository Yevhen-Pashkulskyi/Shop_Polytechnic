from tkinter import END, messagebox

class ListboxManager:
    @staticmethod
    def add_item(listbox, entry_widget, limit=5):
        if listbox.size() >= limit:
            messagebox.showwarning("Ліміт", f"⚠️ Максимальна кількість виробників — {limit}")
            return
        item = entry_widget.get().strip()
        if item:
            listbox.insert(END, item)
            entry_widget.delete(0, END)

    @staticmethod
    def edit_item(listbox, entry_widget):
        try:
            index = listbox.curselection()[0]
            new_value = entry_widget.get().strip()
            if new_value:
                listbox.delete(index)
                listbox.insert(index, new_value)
                entry_widget.delete(0, END)
        except IndexError:
            messagebox.showwarning("⚠️", "Оберіть елемент для редагування.")

    @staticmethod
    def delete_item(listbox):
        try:
            index = listbox.curselection()[0]
            listbox.delete(index)
        except IndexError:
            messagebox.showwarning("⚠️", "Оберіть елемент для видалення.")

    @staticmethod
    def sort_items(listbox):
        items = list(listbox.get(0, END))
        items.sort()
        listbox.delete(0, END)
        for item in items:
            listbox.insert(END, item)

    @staticmethod
    def reverse_items(listbox):
        items = list(listbox.get(0, END))
        items.reverse()
        listbox.delete(0, END)
        for item in items:
            listbox.insert(END, item)
