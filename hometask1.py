# MYHOMETASK 1 
def caching_fibonacci():
    """
    Створює функцію fibonacci(n) з кешуванням результатів
    для ефективного обчислення чисел Фібоначчі.
    """
    cache = {}  # Словник для зберігання обчислених значень

    def fibonacci(n):  # Функція для обчислення n-го числа Фібоначчі
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        # Рекурсивне обчислення та збереження у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
fib = caching_fibonacci()
print(fib(10))  # Виведе: 55
print(fib(15))  # Виведе: 610
