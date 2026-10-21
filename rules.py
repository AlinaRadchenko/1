"""Задача 1. Правила кафе: день тижня і прийом їжі."""
from models import DAYS
from datetime import datetime



def meal_type(hour):
    if 11 <= hour  < 15:
        result = "обід"
    elif 17 <= hour  < 23:
        result = "вечеря"
    else:
        result = "інше"
    return result

    """Прийом їжі за годиною: 11–15 → "обід", 17–23 → "вечеря", решта → "інше".

    >>> meal_type(12), meal_type(16), meal_type(18)
    ('обід', 'інше', 'вечеря')
    """
    raise NotImplementedError("задача 1: напиши meal_type()")

print(meal_type(10))
print(meal_type(14))

def day_name(timestamp):
    return DAYS[timestamp.weekday()]
    """Короткий день тижня з DAYS: datetime(2024, 7, 19, 18, 30) → "пт"."""
    raise NotImplementedError("задача 1: напиши day_name()")

print(day_name(datetime(2024, 7, 19, 18, 30)))