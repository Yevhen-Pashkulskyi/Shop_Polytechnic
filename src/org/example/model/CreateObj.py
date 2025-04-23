from src.org.example.entity.SoccerBall import SoccerBall


class CreateObj:
    @staticmethod
    def create_soccer_ball(name, price, weight, diameter, pressure,
                           manufacturer, material, year, country, image_path):
        return SoccerBall(name, price, weight, diameter, pressure,
                          manufacturer, material, year, country, image_path)
