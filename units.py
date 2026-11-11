from typing import TypedDict


class Unit(TypedDict):
    factor: float
    aliases: tuple[str, ...]


UNITS: dict[str, dict[str, Unit]] = {
    "length": {
        "mm": {
            "factor": 0.001,
            "aliases": ("mm", "мм", "millimeter", "миллиметр", "миллиметры"),
        },
        "cm": {
            "factor": 0.01,
            "aliases": ("cm", "см", "centimeter", "сантиметр", "сантиметры"),
        },
        "m": {
            "factor": 1.0,
            "aliases": ("m", "м", "meter", "метр", "метры"),
        },
        "km": {
            "factor": 1000.0,
            "aliases": ("km", "км", "kilometer", "километр", "километры"),
        },
        "inch": {
            "factor": 0.0254,
            "aliases": ("in", "inch", "inches", "дюйм", "дюймы"),
        },
        "ft": {
            "factor": 0.3048,
            "aliases": ("ft", "foot", "feet", "фут", "футы"),
        },
        "mi": {
            "factor": 1609.344,
            "aliases": ("mi", "mile", "miles", "миля", "мили"),
        },
    },
    "mass": {
        "g": {
            "factor": 0.001,
            "aliases": ("g", "г", "gram", "grams", "грамм", "граммы"),
        },
        "kg": {
            "factor": 1.0,
            "aliases": ("kg", "кг", "kilogram", "килограмм", "килограммы"),
        },
        "lb": {
            "factor": 0.45359237,
            "aliases": ("lb", "lbs", "pound", "pounds", "фунт", "фунты"),
        },
        "oz": {
            "factor": 0.028349523125,
            "aliases": ("oz", "ounce", "ounces", "унция", "унции"),
        },
    },
}
