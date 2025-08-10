#Myhomework 2 
import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує дійсні числа з тексту як float, які чітко відокремлені пробілами.
    :param text: Вхідний рядок з текстом.
    :yield: Дійсні числа у форматі float.
    """
    # Знаходить усі числа (цілі та дробові), чітко обмежені пробілами
    pattern = r'\s(\d+\.\d+|\d+)\s'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підсумовує всі дійсні числа з тексту, використовуючи передану функцію генерації.
    :param text: Вхідний рядок з текстом.
    :param func: Функція, яка повертає генератор чисел.
    :return: Загальна сума чисел.
    """
    return sum(func(text))

text = ("Загальний дохід працівника складається
