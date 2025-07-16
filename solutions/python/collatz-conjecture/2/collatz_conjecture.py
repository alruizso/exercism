def calculate_steps(number: int) -> int:
    steps = 0
    next_iter = number
    while next_iter != 1:
        if bool(next_iter%2):
            next_iter = next_iter * 3 + 1
            steps += 1
            continue
        next_iter = next_iter // 2
        steps += 1
        continue
    
    return steps
        
    
def steps(number: int) -> int:
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    return calculate_steps(number)
