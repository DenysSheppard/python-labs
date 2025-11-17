def custom_sort_key(s):
    s_lower = s.lower()
    if not s_lower:
        return (2, "")

    first_char = s_lower[0]

    if 'а' <= first_char <= 'я' or first_char in 'іїєґ':
        group = 0
    elif 'a' <= first_char <= 'z':
        group = 1
    else:
        group = 2

    return (group, s_lower)

initial_list = [
    'English', 'інформація', 'android', 'Windows', 
    'Добрий день', 'матриця', 'актова зала', 'біоресурси', 
    'єдиний', 'кава', 'Історія', 'Їжак', 'apple'
]

print("Заданий список:")
print(initial_list)

sorted_list = sorted(initial_list, key=custom_sort_key)

print("\nВідсортований список:")
print(sorted_list)