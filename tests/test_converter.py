import pytest

from converter import convert


@pytest.mark.parametrize(
    ("value", "from_unit", "to_unit", "expected"),
    [
        (1, "km", "m", 1000),
        (1, "дюйм", "мм", 25.4),
        (1, "ft", "m", 0.3048),
        (1, "mi", "km", 1.609344),
        (1, "kg", "g", 1000),
        (1, "lb", "kg", 0.45359237),
        (1, "oz", "g", 28.349523125),
        (100, "см", "m", 1),
        (1, "M", "CM", 100),
    ],
)
def test_convert_supported_units(value, from_unit, to_unit, expected):
    assert convert(value, from_unit, to_unit) == pytest.approx(expected)


def test_convert_returns_float_for_same_unit():
    assert convert(3, "m", "m") == pytest.approx(3.0)


def test_convert_rejects_unknown_unit():
    with pytest.raises(ValueError, match="Неизвестная единица"):
        convert(1, "parsec", "m")


def test_convert_rejects_different_categories():
    with pytest.raises(ValueError, match="разным категориям"):
        convert(1, "m", "kg")
