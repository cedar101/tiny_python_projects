def english_enumerate(items: list[str], serial_comma=False) -> str:
    num = len(items)
    if num == 0:
        return ""
    if num == 1:
        return items[0]
    if serial_comma:
        if num == 2:
            return " and ".join(items)
        items[-1] = f"and {items[-1]}"
        return ", ".join(items)
    else:
        return f"{', '.join(items[:-1])} and {items[-1]}"
