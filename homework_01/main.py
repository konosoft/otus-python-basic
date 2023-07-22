"""
Домашнее задание №1
Функции и структуры данных
"""
import math
from typing import List

def power_numbers(*nums: int) -> List[int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num > 1

def filter_numbers(numbers_list: List[int], filter_type: str) -> List[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    # В одну строчку
    # return list(filter(lambda x:
    #                    x % 2 if filter_type == ODD
    #                    else x % 2 == 0 if filter_type == EVEN
    #                    else is_prime(x) if filter_type == PRIME
    #                    else None
    #                    , numbers_list))

    # Читаемее
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2]
    if filter_type == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))
