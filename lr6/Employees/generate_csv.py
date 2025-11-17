import csv
import random
from faker import Faker
from datetime import date, timedelta, datetime

fake = Faker(locale='uk_UA')
random.seed(1)
Faker.seed(1)

NUM_RECORDS = 500
PCT_FEMALE = 0.40

patronymics_male = [
    "Іванович","Петрович","Сергійович","Миколайович","Олександрович",
    "Васильович","Андрійович","Григорович","Євгенович","Ігорович",
    "Степанович","Павлович","Романович","Анатолійович","Володимирович",
    "Тарасович","Олексійович","Борисович","Юрійович","Михайлович"
]

patronymics_female = [
    "Іванівна","Петрівна","Сергіївна","Миколаївна","Олександрівна",
    "Василівна","Андріївна","Григорівна","Євгенівна","Ігорівна",
    "Степанівна","Павлівна","Романівна","Анатоліївна","Володимирівна",
    "Тарасівна","Олексіївна","Борисівна","Юріївна","Михайлівна"
]

positions = [
    "Інженер", "Технік", "Менеджер", "Бухгалтер", "Адміністратор",
    "Керівник відділу", "Працівник складу", "Оператор", "Програміст",
    "Маркетолог", "Аналітик", "Лаборант", "Секретар", "HR", "ІТ-спеціаліст"
]

cities = [fake.city() for _ in range(20)]

def random_date(start_year=1938, end_year=2008):
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    delta = end - start
    random_day = random.randrange(delta.days + 1)
    return start + timedelta(days=random_day)

def gen_record(is_female):
    if is_female:
        first_name = fake.first_name_female()
        patronymic = random.choice(patronymics_female)
        sex = "Ж"
    else:
        first_name = fake.first_name_male()
        patronymic = random.choice(patronymics_male)
        sex = "Ч"
    last_name = fake.last_name()
    dob = random_date().strftime("%Y-%m-%d")
    position = random.choice(positions)
    city = random.choice(cities)
    address = fake.street_address()
    phone = fake.phone_number()
    email = fake.email()
    return [last_name, first_name, patronymic, sex, dob, position, city, address, phone, email]

def main():
    num_female = int(NUM_RECORDS * PCT_FEMALE)
    num_male = NUM_RECORDS - num_female
    rows = []

    genders = ["F"] * num_female + ["M"] * num_male
    random.shuffle(genders)
    for g in genders:
        rows.append(gen_record(is_female=(g == "F")))

    header = ["Прізвище","Ім'я","По_батькові","Стать","Дата_народження","Посада","Місто","Адреса","Телефон","Email"]
    with open("employees.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"CSV файл 'employees.csv' згенеровано успішно ({NUM_RECORDS} записів).")

if __name__ == "__main__":
    main()