def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Not a valid square")
    return 2 ** (number - 1)


def total():
    return sum(square(x) for x in range(1, 65))
