# MYHOMETASK 2
import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує дійсні числа з тексту як float, які чітко відокремлені пробілами.
    :param text: Вхідний рядок з текстом.
    :yield: Дійсні числа у форматі float.
    """
    # Знаходить усі дійсні числа обмежені пробілами
    for match in re.findall(r'\b\d+\.\d+\b', text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підсумовує всі дійсні числа з тексту, використовуючи передану функцію генерації.
    
    :param text: Вхідний рядок з текстом.
    :param func: Функція, яка повертає генератор чисел.
    :return: Загальна сума чисел.
    """
    return sum(func(text))
text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")