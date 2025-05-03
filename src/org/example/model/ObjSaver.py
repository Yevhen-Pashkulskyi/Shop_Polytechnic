import csv
import json
import os
import pickle

from src.org.example.model.CreateObj import CreateObj


class ObjSaver:
    BASE_DIR = "../../../resource/Ivanov"
    NAME_FILE = "soccer_balls"
    JSON_FILE = os.path.join(BASE_DIR, NAME_FILE + ".json")
    TXT_FILE = os.path.join(BASE_DIR, NAME_FILE + ".txt")
    CSV_FILE = os.path.join(BASE_DIR, NAME_FILE + ".csv")
    BIN_FILE = os.path.join(BASE_DIR, NAME_FILE + ".bin")

    @staticmethod
    def ensure_directory():
        if not os.path.exists(ObjSaver.BASE_DIR):
            os.makedirs(ObjSaver.BASE_DIR)

    # @staticmethod
    # def save_all_formats(objects):
    #     ObjSaver.ensure_directory()
    #     ObjSaver.save_txt(objects)

    # @staticmethod
    # def save_txt(objects):
    #     with open(f"{ObjSaver.DIRECTORY_PATH}/objects.txt", "w", encoding="utf-8") as f:
    #         for obj in objects:
    #             for key, val in obj.items():
    #                 f.write(f"{key}: {val}\n")
    #             f.write("-"*30 + "\n")
    #
    # @staticmethod
    # def save_csv(objects):
    #     if not objects:
    #         return
    #     with open(f"{ObjSaver.DIRECTORY_PATH}/objects.csv", "w", encoding="utf-8") as f:
    #         writer = csv.DictWriter(f, fieldnames=objects[0].keys())
    #         writer.writeheader()
    #         writer.writerows(objects)
    #
    # @staticmethod
    # def save_bin(objects):
    #     with open(f"{ObjSaver.DIRECTORY_PATH}/objects.bin", "wb") as f:
    #         pickle.dump(objects, f)
    #
    # @staticmethod
    # def load_bin():
    #     with open(f"{ObjSaver.DIRECTORY_PATH}/objects.bin", "rb") as f:
    #         return pickle.load(f)
    #
    # @staticmethod
    # def load_csv():
    #     with open(f"{ObjSaver.DIRECTORY_PATH}/objects.csv", "r", encoding="utf-8") as f:
    #         reader = csv.DictReader(f)
    #         return list(reader)
    #
    # @staticmethod
    # def load_txt():
    #     objects = []
    #     with open(f"{ObjSaver.DIRECTORY_PATH}/objects.txt", "r", encoding="utf-8") as f:
    #         obj = {}
    #         for line in f:
    #             line = line.strip()
    #             if line == "-"*30:
    #                 if obj:
    #                     objects.append(obj)
    #                     obj = {}
    #             elif ":" in line:
    #                 key, val = line.split(": ", 1)
    #                 obj[key] = val.strip()
    #     return objects

    @staticmethod
    def save(ball_obj):
        ObjSaver.ensure_directory()
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
        # save to JSON
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

        # Save to TXT
        with open(ObjSaver.TXT_FILE, "a", encoding="utf-8") as file:
            file.write(f"Name: {data['name']}, Price: {data['price']}, Weight: {data['weight']}, "
                       f"Diameter: {data['diameter']}, Pressure: {data['pressure']}, "
                       f"Manufacturer: {data['manufacturer']}, Material: {data['material']}, "
                       f"Year: {data['year']}, Country: {data['country']}, Image: {data['image_path']}\n")
        # Save to CSV
        csv_headers = ["name", "price", "weight", "diameter", "pressure", "manufacturer", "material", "year", "country",
                       "image_path"]
        file_exists = os.path.exists(ObjSaver.CSV_FILE)
        with open(ObjSaver.CSV_FILE, "a", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_headers)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)

        # Save to BIN
        balls = ObjSaver.load_all()  # Load existing balls to append
        balls.append(ball_obj)
        with open(ObjSaver.BIN_FILE, "wb") as file:
            pickle.dump(balls, file)

    @staticmethod
    def load_all():
        ObjSaver.ensure_directory()
        balls = []
        # load from JSON
        if os.path.exists(ObjSaver.JSON_FILE):
            with open(ObjSaver.JSON_FILE, "r", encoding="utf-8") as file:
                try:
                    data_list = json.load(file)
                    return [CreateObj.create_soccer_ball(**data) for data in data_list]
                except json.JSONDecodeError:
                    balls = []
        # Load from TXT (for verification, but JSON is primary)
        txt_balls = []
        if os.path.exists(ObjSaver.TXT_FILE):
            with open(ObjSaver.TXT_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    try:
                        parts = line.strip().split(", ")
                        data = {}
                        for part in parts:
                            key, value = part.split(": ", 1)
                            data[key.lower().replace(" ", "_")] = value
                        txt_balls.append(CreateObj.create_soccer_ball(**data))
                    except Exception:
                        continue

        # Load from CSV
        csv_balls = []
        if os.path.exists(ObjSaver.CSV_FILE):
            with open(ObjSaver.CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    csv_balls.append(CreateObj.create_soccer_ball(**row))

        # Load from BIN
        bin_balls = []
        if os.path.exists(ObjSaver.BIN_FILE):
            with open(ObjSaver.BIN_FILE, "rb") as file:
                try:
                    bin_balls = pickle.load(file)
                except Exception:
                    bin_balls = []

        # Return JSON data as primary, but warn if others differ
        from tkinter import messagebox
        if txt_balls and len(txt_balls) != len(balls):
            messagebox.showwarning("Увага", "Дані у файлі TXT не відповідають JSON")
        if csv_balls and len(csv_balls) != len(balls):
            messagebox.showwarning("Увага", "Дані у файлі CSV не відповідають JSON")
        if bin_balls and len(bin_balls) != len(balls):
            messagebox.showwarning("Увага", "Дані у файлі BIN не відповідають JSON")

        return balls

    @staticmethod
    def delete(ball_name):
        ObjSaver.ensure_directory()
        success = False
        # delete from JSON
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

        # Delete from TXT
        if os.path.exists(ObjSaver.TXT_FILE):
            with open(ObjSaver.TXT_FILE, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(ObjSaver.TXT_FILE, "w", encoding="utf-8") as file:
                for line in lines:
                    if f"Name: {ball_name}" not in line:
                        file.write(line)
                success = True

        # Delete from CSV
        if os.path.exists(ObjSaver.CSV_FILE):
            with open(ObjSaver.CSV_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                rows = [row for row in reader if row["name"] != ball_name]
            with open(ObjSaver.CSV_FILE, "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
                success = True

        # Delete from BIN
        if os.path.exists(ObjSaver.BIN_FILE):
            balls = ObjSaver.load_all()
            balls = [ball for ball in balls if ball.name != ball_name]
            with open(ObjSaver.BIN_FILE, "wb") as file:
                pickle.dump(balls, file)
                success = True

        return success
