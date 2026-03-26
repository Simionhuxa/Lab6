import json

students = {
    "Simionenko": ["Dasha", "Oleksandrivna", 2005],
    "Іваненко": ["Іван", "Іванович", 2001],
    "Петренко": ["Петро", "Петрович", 2002],
    "Шевченко": ["Марія", "Іванівна", 2000],
    "Коваленко": ["Олена", "Сергіївна", 2003],
    "Мельник": ["Андрій", "Миколайович", 2001],
    "Бондаренко": ["Ірина", "Петрівна", 2004],
    "Ткаченко": ["Оксана", "Василівна", 2002],
    "Романенко": ["Дмитро", "Олегович", 2000],
    "Кравченко": ["Наталія", "Юріївна", 2003]
}

# запис у JSON
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

print("Файл students.json створено")

# читання з JSON
with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("\nДані з файлу:\n")

for surname, info in data.items():
    print(f"{surname}: {info[0]} {info[1]}, {info[2]}")