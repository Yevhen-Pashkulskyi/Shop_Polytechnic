import csv
import json
import os
import pickle
from tkinter import messagebox

from src.org.example.model.CreateObj import CreateObj

class ObjSaver:
    BASE_DIR = "../../../resource/Pashkulskyi"
    NAME_FILE = "soccer_balls"
    JSON_FILE = os.path.join(BASE_DIR, NAME_FILE + ".json")
    TXT_FILE = os.path.join(BASE_DIR, NAME_FILE + ".txt")
    CSV_FILE = os.path.join(BASE_DIR, NAME_FILE + ".csv")
    BIN_FILE = os.path.join(BASE_DIR, NAME_FILE + ".bin")

    @staticmethod
    def ensure_directory():
        if not os.path.exists(ObjSaver.BASE_DIR):
            os.makedirs(ObjSaver.BASE_DIR)

    @staticmethod
    def save(ball_obj):
        ObjSaver.ensure_directory()
        data = {"name": ball_obj.name, "price": ball_obj.price, "weight": ball_obj.weight,
            "diameter": ball_obj.diameter, "pressure": ball_obj.pressure, "manufacturer": ball_obj.manufacturer,
            "material": ball_obj.material, "year": ball_obj.year, "country": ball_obj.country,
            "image_path": ball_obj.image_path}

        if not os.path.exists(ObjSaver.JSON_FILE):
            with open(ObjSaver.JSON_FILE, "w", encoding="utf-8") as file:
                json.dump([data], file, indent=4, ensure_ascii=False)
        else:
            with open(ObjSaver.JSON_FILE, "r+", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                    content.append(data)
                    file.seek(0)
                    json.dump(content, file, indent=4, ensure_ascii=False)
                except json.JSONDecodeError:
                    json.dump([data], file, indent=4, ensure_ascii=False)

        with open(ObjSaver.TXT_FILE, "a", encoding="utf-8") as file:
            file.write(f"Name: {data['name']}, Price: {data['price']}, Weight: {data['weight']}, "
                       f"Diameter: {data['diameter']}, Pressure: {data['pressure']}, "
                       f"Manufacturer: {data['manufacturer']}, Material: {data['material']}, "
                       f"Year: {data['year']}, Country: {data['country']}, Image_path: {data['image_path']}\n")

        csv_headers = ["name", "price", "weight", "diameter", "pressure", "manufacturer", "material", "year", "country",
                       "image_path"]
        file_exists = os.path.exists(ObjSaver.CSV_FILE)
        with open(ObjSaver.CSV_FILE, "a", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        balls = ObjSaver.load_all(source="bin")  # Load existing balls to append
        balls.append(ball_obj)
        with open(ObjSaver.BIN_FILE, "wb") as file:
            pickle.dump(balls, file)

    @staticmethod
    def load_all(source="json"):
        ObjSaver.ensure_directory()
        balls = []
        if source == "json" and os.path.exists(ObjSaver.JSON_FILE):
            with open(ObjSaver.JSON_FILE, "r", encoding="utf-8") as file:
                try:
                    data_list = json.load(file)
                    balls = [CreateObj.create_soccer_ball(**data) for data in data_list]
                except json.JSONDecodeError:
                    messagebox.showerror("Помилка", "Не вдалося прочитати JSON файл")
                    balls = []

        elif source == "txt" and os.path.exists(ObjSaver.TXT_FILE):
            with open(ObjSaver.TXT_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    try:
                        parts = line.strip().split(", ")
                        data = {}
                        for part in parts:
                            key, value = part.split(": ", 1)
                            data[key.lower().replace(" ", "_")] = value
                        balls.append(CreateObj.create_soccer_ball(**data))
                    except Exception:
                        continue

        elif source == "csv" and os.path.exists(ObjSaver.CSV_FILE):
            with open(ObjSaver.CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    balls.append(CreateObj.create_soccer_ball(**row))

        elif source == "bin" and os.path.exists(ObjSaver.BIN_FILE):
            with open(ObjSaver.BIN_FILE, "rb") as file:
                try:
                    balls = pickle.load(file)
                except Exception:
                    messagebox.showerror("Помилка", "Не вдалося прочитати BIN файл")
                    balls = []

        return balls

    @staticmethod
    def delete(ball_name):
        ObjSaver.ensure_directory()
        success = False

        if os.path.exists(ObjSaver.JSON_FILE):
            with open(ObjSaver.JSON_FILE, "r+", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                    updated_content = [item for item in content if item["name"] != ball_name]
                    file.seek(0)
                    file.truncate()
                    json.dump(updated_content, file, indent=4, ensure_ascii=False)
                    success = True
                except json.JSONDecodeError:
                    success = False

        if os.path.exists(ObjSaver.TXT_FILE):
            with open(ObjSaver.TXT_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(ObjSaver.TXT_FILE, "w", encoding="utf-8") as file:
                for line in lines:
                    if f"Name: {ball_name}" not in line:
                        file.write(line)
                success = True

        if os.path.exists(ObjSaver.CSV_FILE):
            with open(ObjSaver.CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                rows = [row for row in reader if row["name"] != ball_name]
            with open(ObjSaver.CSV_FILE, "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
                success = True

        if os.path.exists(ObjSaver.BIN_FILE):
            balls = ObjSaver.load_all()
            balls = [ball for ball in balls if ball.name != ball_name]
            with open(ObjSaver.BIN_FILE, "wb") as file:
                pickle.dump(balls, file)
                success = True

        return success
