def gen_list() -> list:
    count = 0
    previous_item = 1
    squares = []
    while count < 64:
        squares.append(previous_item)
        count += 1
        previous_item = previous_item * 2
    return squares

squares_list = gen_list()

def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return(squares_list[number-1])

def total():
    return sum(squares_list)
