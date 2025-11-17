import json

file_name = 'people.json'

try:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"Дані, успішно прочитані з файлу '{file_name}':\n")
    
    for surname, info in data.items():
        print(f"Прізвище: {surname}")
        print(f"  Ім'я: {info[0]}")
        print(f"  По батькові: {info[1]}")
        print(f"  Рік народження: {info[2]}")
        print("-" * 25)

except FileNotFoundError:
    print(f"Помилка: Файл '{file_name}' не знайдено.")
    print("Будь ласка, спочатку запустіть 'program2_write_json.py'.")
except json.JSONDecodeError:
    print(f"Помилка: Не вдалося прочитати JSON з файлу '{file_name}'.")