from src.org.example.model.ObjSaver import ObjSaver
from src.org.example.model.CreateObj import CreateObj
from src.org.example.view.GUIBuilder import GUIBuilder
from src.org.example.view.GalleryView import GalleryView

class Control:
    def __init__(self):
        self.gui = None
        self.gallery = None
        self.loaded_objects = []
        self.current_loaded_index = 0

    def init_gui(self, root):


        self.gui = GUIBuilder(root, self)
        self.gallery = GalleryView(self.gui.input_tab)
        self.gui.set_gallery_view(self.gallery)
        self.gallery.show_image_ball()
        self.load_objects()

    def create_soccer_ball(self):
        try:
            name = self.gui.name_entry.get().strip()
            if not name:
                raise ValueError("⛔ Поле «Назва» не може бути порожнім.")

            price = self.get_float(self.gui.price_entry, "Ціна (грн)")
            weight = self.get_float(self.gui.weight_entry, "Вага (кг)")
            diameter = self.get_float(self.gui.diameter_entry, "Діаметр (см)")
            pressure = self.get_float(self.gui.pressure_entry, "Тиск (атм)")

            manufacturer = self.get_selected_listbox_value(self.gui.manufacturer_listbox, "виробника")
            material = self.gui.selected_material.get()
            year = self.gui.selected_year.get()
            country = self.gui.selected_country.get()
            image_path = self.gallery.get_current_image_path()

            ball = CreateObj.create_soccer_ball(name, price, weight, diameter, pressure,
                                                manufacturer, material, year, country, image_path)

            ObjSaver.save(ball)
            self.gui.result_label.config(text=ball.getInfo())
            self.gui.update_result_image(image_path)
            self.load_objects()

        except ValueError as ve:
            from tkinter import messagebox
            messagebox.showerror("Помилка валідації", str(ve))
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Помилка", f"⚠️ Сталася помилка: {e}")

    def load_objects(self):
        self.loaded_objects = ObjSaver.load_all()
        if self.loaded_objects:
            self.show_object(0)
        else:
            self.gui.result_label.config(text="Об'єкти відсутні")
            self.gui.result_image_label.config(image='', text="❌")

    def show_object(self, index):
        if 0 <= index < len(self.loaded_objects):
            ball = self.loaded_objects[index]
            self.gui.result_label.config(text=ball.getInfo())
            self.gui.update_result_image(ball.image_path)
            self.current_loaded_index = index

    def show_next_loaded_object(self):
        if self.loaded_objects:
            self.current_loaded_index = (self.current_loaded_index + 1) % len(self.loaded_objects)
            self.show_object(self.current_loaded_index)

    def show_previous_loaded_object(self):
        if self.loaded_objects:
            self.current_loaded_index = (self.current_loaded_index - 1) % len(self.loaded_objects)
            self.show_object(self.current_loaded_index)

    def delete_current_object(self):
        if not self.loaded_objects:
            return

        from tkinter import messagebox
        ball = self.loaded_objects[self.current_loaded_index]
        confirm = messagebox.askyesno("Підтвердження", f"Ви впевнені, що хочете видалити '{ball.name}'?")
        if confirm:
            if ObjSaver.delete(ball.name):
                messagebox.showinfo("Успішно", f"Об'єкт '{ball.name}' видалено")
                self.load_objects()
            else:
                messagebox.showerror("Помилка", f"Не вдалося видалити '{ball.name}'")

    def get_selected_listbox_value(self, listbox, label):
        try:
            index = listbox.curselection()[0]
            return listbox.get(index)
        except IndexError:
            raise ValueError(f"⛔ Оберіть значення {label} зі списку.")

    def get_float(self, entry, label_name):
        value = entry.get().strip()
        if not value:
            raise ValueError(f"⛔ Поле «{label_name}» не може бути порожнім.")
        try:
            float_value = float(value)
        except ValueError:
            raise ValueError(f"⛔ Поле «{label_name}» повинно містити число.")
        if float_value <= 0:
            raise ValueError(f"⛔ Значення «{label_name}» не може бути від'ємним.")
        return float_value
