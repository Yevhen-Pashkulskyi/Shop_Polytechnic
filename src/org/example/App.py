from tkinter import Tk

from src.org.example.control.Control import Control
from src.org.example.view.GUIBuilder import GUIBuilder
from src.org.example.view.GalleryView import GalleryView


class App:
    def __init__(self, root):
        self.view = GalleryView(root)
        self.gui = GUIBuilder(root, self.view)
        self.view.show_image()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
