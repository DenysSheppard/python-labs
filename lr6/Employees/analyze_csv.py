import pandas as pd
import sys
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "employees.csv"

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

def main():
    try:
        df = pd.read_csv(CSV_FILE, encoding="utf-8")
        print("Ok — CSV файл відкрито.")
    except Exception as e:
        print("Помилка при відкритті CSV файлу:", e)
        sys.exit(1)

    df['Вік'] = df['Дата_народження'].apply(calculate_age)
    df['Категорія'] = df['Вік'].apply(age_category)

    sex_counts = df['Стать'].value_counts()
    print("Кількість за статтю:")
    print(sex_counts)

    plt.figure()
    sex_counts.plot(kind='bar')
    plt.title("Кількість співробітників за статтю")
    plt.xlabel("Стать (Ч = чоловіки, Ж = жінки)")
    plt.ylabel("Кількість")
    plt.tight_layout()
    plt.savefig("sex_counts.png")
    print("Збережено графік: sex_counts.png")

    age_cat_counts = df['Категорія'].value_counts().reindex(["younger_18","18-45","45-70","older_70"]).fillna(0)
    print("\nКількість за віковими категоріями:")
    print(age_cat_counts)

    plt.figure()
    age_cat_counts.plot(kind='bar')
    plt.title("Кількість по віковим категоріям")
    plt.xlabel("Вікова категорія")
    plt.ylabel("Кількість")
    plt.tight_layout()
    plt.savefig("age_category_counts.png")
    print("Збережено графік: age_category_counts.png")

    print("\nКількість за статтю у кожній віковій категорії:")
    cross = pd.crosstab(df['Категорія'], df['Стать']).reindex(index=["younger_18","18-45","45-70","older_70"]).fillna(0)
    print(cross)

    for cat in ["younger_18","18-45","45-70","older_70"]:
        if cat in cross.index:
            plt.figure()
            cross.loc[cat].plot(kind='bar')
            plt.title(f"Стать у категорії {cat}")
            plt.xlabel("Стать")
            plt.ylabel("Кількість")
            plt.tight_layout()
            fname = f"sex_in_{cat}.png"
            plt.savefig(fname)
            print(f"Збережено графік: {fname}")

    print("\nАналіз завершено.")

if __name__ == "__main__":
    main()