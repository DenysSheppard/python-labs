numbers = [2, 3, 7, 2, 1, 0, 5, 2, 3, 1, 8, 4, 8]
A = 10

found = []
max_len = 0

for start in range(len(numbers)):
    total = 0
    for end in range(start, len(numbers)):
        total += numbers[end]
        if total == A:
            subarray = numbers[start:end+1]
            found.append(subarray)
            max_len = max(max_len, len(subarray))
        elif total > A:
            break

print("Підрядки з сумою A = {}:".format(A))
for sub in found:
    print(sub)

print(f"Максимальна кількість елементів: {max_len}")