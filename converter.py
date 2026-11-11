from units import UNITS


_UNIT_INDEX = {
    alias.casefold(): (category, unit["factor"])
    for category, category_units in UNITS.items()
    for unit in category_units.values()
    for alias in unit["aliases"]
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Конвертирует значение между единицами длины или массы."""
    source = _UNIT_INDEX.get(from_unit.strip().casefold())
    if source is None:
        raise ValueError(f"Неизвестная единица: {from_unit}")

    target = _UNIT_INDEX.get(to_unit.strip().casefold())
    if target is None:
        raise ValueError(f"Неизвестная единица: {to_unit}")

    source_category, source_factor = source
    target_category, target_factor = target
    if source_category != target_category:
        raise ValueError("Единицы относятся к разным категориям")

    return value * source_factor / target_factor
