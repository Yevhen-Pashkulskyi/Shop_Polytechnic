from src.org.example.entity.SoccerBall import SoccerBall


class CreateObj:
    def __init__(self, gui, view):
        self.gui = gui
        self.view = view

    def create_object(self):
        try:
            name = self.gui.name_entry.get()
            price = float(self.gui.price_entry.get())
            weight = float(self.gui.weight_entry.get())
            diameter = float(self.gui.diameter_entry.get())
            pressure = float(self.gui.pressure_entry.get())  # window

            football = SoccerBall(name, price, weight, diameter, pressure)
            self.gui.result_label.config(text=football.getInfo())

        except ValueError:
            self.result_label.config(text="❌ Помилка: перевірте введені дані!")
