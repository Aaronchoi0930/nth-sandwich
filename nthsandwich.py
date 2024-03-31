def isSandwich(num):
    for i in range(1, num)
        if num % 10 == 0:
            return False

    first_digit = num // 100
    last_digit = num % 10

    if first_digit != last_digit:
        return False

    return True