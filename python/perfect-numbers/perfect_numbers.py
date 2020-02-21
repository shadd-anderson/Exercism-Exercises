def classify(number):
    if number < 1:
        raise ValueError("We can only test for factors of natural integers")

    sum_factors = sum(get_factors(number))
    if sum_factors == number:
        return "perfect"
    elif sum_factors > number:
        return "abundant"
    else:
        return "deficient"


def get_factors(number):
    factors = set()
    for x in range(1, number // 2 + 1):
        if number % x == 0:
            factors.add(x)
    return factors
