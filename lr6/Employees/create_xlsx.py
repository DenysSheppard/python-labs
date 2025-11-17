import pandas as pd
from datetime import datetime
import sys

CSV_FILE = "employees.csv"
XLSX_FILE = "employees_by_age.xlsx"

def calculate_age(born_str):
    born = datetime.strptime(born_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

def age_category(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 46 <= age <= 70:
        return "45-70"
    else:
        return "older_70"

def create_sheet(df, writer, sheet_name):
    """Створює аркуш з правильною структурою."""
    
    formatted_df = pd.DataFrame({
        "№": range(1, len(df) + 1),
        "Прізвище": df["Прізвище"],
        "Ім’я": df["Ім'я"],
        "По батькові": df["По_батькові"],
        "Дата народження": df["Дата_народження"],
        "Вік": df["Вік"]
    })

    formatted_df.to_excel(writer, sheet_name=sheet_name, index=False)


def main():
    try:
        df = pd.read_csv(CSV_FILE, encoding="utf-8")
    except Exception as e:
        print("Помилка при відкритті CSV файлу:", e)
        print("Повідомлення: CSV_ERROR")
        sys.exit(1)

    df['Вік'] = df['Дата_народження'].apply(calculate_age)

    df['Категорія'] = df['Вік'].apply(age_category)

    try:
        with pd.ExcelWriter(XLSX_FILE, engine='openpyxl') as writer:

            # --- Аркуш "all": записуємо ВСІ колонки без змін ---
            df.to_excel(writer, sheet_name="all", index=False)

            # --- Інші аркуші: тільки структура з картинки ---
            create_sheet(df[df['Категорія'] == "younger_18"], writer, "younger_18")
            create_sheet(df[df['Категорія'] == "18-45"], writer, "18-45")
            create_sheet(df[df['Категорія'] == "45-70"], writer, "45-70")
            create_sheet(df[df['Категорія'] == "older_70"], writer, "older_70")

    except Exception as e:
        print("Повідомлення: Неможливо створити XLSX файл:", e)
        sys.exit(1)

    print("Ok — XLSX файл створено успішно:", XLSX_FILE)


if __name__ == "__main__":
    main()