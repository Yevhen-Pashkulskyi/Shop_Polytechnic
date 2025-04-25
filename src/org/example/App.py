from tkinter import Tk
from src.org.example.control.Control import Control

class App:
    def __init__(self, root):
        self.control = Control()
        self.control.init_gui(root)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
