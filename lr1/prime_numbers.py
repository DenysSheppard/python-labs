def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

start = min(a, b)
end = max(a, b)

print(f"Прості числа між {start} і {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=' ')