from src.org.example.entity.Ball import Ball


class CreateObj:
    @staticmethod
    def create_soccer_ball(name, price, weight, diameter, pressure,
                           manufacturer, material, year, country, image_path):
        return Ball(name, price, weight, diameter, pressure,
                    manufacturer, material, year, country, image_path)
