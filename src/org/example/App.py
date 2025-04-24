from tkinter import Tk

from src.org.example.view.GUIBuilder import GUIBuilder
from src.org.example.view.GalleryView import GalleryView


class App:
    def __init__(self, root):
        self.gui = GUIBuilder(root)
        self.view = GalleryView(self.gui.input_tab)
        self.gui.set_gallery_view(self.view)
        self.view.show_image_ball()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
