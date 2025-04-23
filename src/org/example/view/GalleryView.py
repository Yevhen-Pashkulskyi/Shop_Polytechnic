from tkinter import *
from PIL import Image, ImageTk


class GalleryView:
    def __init__(self, parent_frame):
        # Галерея зображень
        self.image_paths = ["../../../resource/img/ball1.png",
                            "../../../resource/img/ball2.png",
                            "../../../resource/img/ball3.png"]
        self.current_index = 0
        self.image_label = Label(parent_frame)
        self.image_label.grid(row=15, column=0, columnspan=2, pady=10)

    def show_image(self):
        try:
            img = Image.open(self.image_paths[self.current_index])
            img = img.resize((250, 150))
            self.tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.tk_img)
        except Exception as e:
            self.image_label.config(text=f"Помилка завантаження зображення\n{e}")

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.show_image()

    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_paths)
        self.show_image()

    def clear_image(self):
        self.image_label.config(text="")
        self.current_index = 0
        self.show_image()

    def get_current_image_path(self):
        return self.image_paths[self.current_index]
