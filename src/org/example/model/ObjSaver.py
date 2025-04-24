import json
import os

from src.org.example.model.CreateObj import CreateObj


class ObjSaver:
    FILE_PATH = "../../../resource/soccer_balls.json"

    @staticmethod
    def save(ball_obj):
        data = {
            "name": ball_obj.name,
            "price": ball_obj.price,
            "weight": ball_obj.weight,
            "diameter": ball_obj.diameter,
            "pressure": ball_obj.pressure,
            "manufacturer": ball_obj.manufacturer,
            "material": ball_obj.material,
            "year": ball_obj.year,
            "country": ball_obj.country,
            "image_path": ball_obj.image_path
        }

        if not os.path.exists(ObjSaver.FILE_PATH):
            with open(ObjSaver.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump([data], file, indent=4, ensure_ascii=False)
        else:
            with open(ObjSaver.FILE_PATH, "r+", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                    content.append(data)
                    file.seek(0)
                    json.dump(content, file, indent=4, ensure_ascii=False)
                except json.JSONDecodeError:
                    json.dump([data], file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_all():
        if os.path.exists(ObjSaver.FILE_PATH):
            with open(ObjSaver.FILE_PATH, "r", encoding="utf-8") as file:
                try:
                    data_list = json.load(file)
                    return [CreateObj.create_soccer_ball(**data) for data in data_list]
                except json.JSONDecodeError:
                    return []
        else:
            return []

    @staticmethod
    def delete(ball_name):
        if os.path.exists(ObjSaver.FILE_PATH):
            with open(ObjSaver.FILE_PATH, "r+", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                    updated_content = [item for item in content if item["name"] != ball_name]
                    file.seek(0)
                    file.truncate() # Очищаємо вміст файлу перед записом оновлених даних
                    json.dump(updated_content, file, indent=4, ensure_ascii=False)
                    return True # Повертаємо True, якщо об'єкт був знайдений і видалений
                except json.JSONDecodeError:
                    return False # Повертаємо False, якщо файл порожній або містить некоректний JSON
        else:
            return False # Повертаємо False, якщо файл не існує