"""Задача 2. Розбір одного рядка каси."""
from datetime import datetime

from models import RawOrder

def parse_line(line):
    """Рядок "2024-07-19 18:30;540.00;50;2" → RawOrder.

    Поля через ";": час "%Y-%m-%d %H:%M", сума, чайові, кількість гостей.
    Зіпсований рядок → ValueError з поясненням людською мовою:
    не 4 поля, не число, неіснуюча дата, сума <= 0, чайові < 0, гостей < 1.
    """

    try:
        time_text, bill_text, tip_text, size_text = line.split(";")
        timestamp = datetime.strptime(time_text, "%Y-%m-%d %H:%M")
        float(bill_text)
        float(tip_text)
        int(size_text)
    except ValueError:
        raise ValueError("Некоректна дата або числові дані.")

    if float(bill_text) <= 0:
        raise ValueError("Сума чека має бути більшою за 0.")

    if float(tip_text) < 0:
        raise ValueError("Чайові не можуть бути від’ємними.")

    if int(size_text) < 1:
        raise ValueError("Кількість гостей має бути не меншою за 1.")

    return RawOrder(float(bill_text), float(tip_text), int(size_text), timestamp)

print(parse_line("2024-07-19 18:30;540.00;50;2"))

