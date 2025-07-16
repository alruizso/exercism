def is_armstrong_number(number: int) -> bool:
    number = f"{number}"
    total = 0
    length = len(number)
    for item in number:
        total += int(item) ** length

    if total == int(number):
        return True
    return False
