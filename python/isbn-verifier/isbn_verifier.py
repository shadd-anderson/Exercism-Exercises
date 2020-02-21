def is_valid(isbn):
    if len(isbn.replace("-", "")) != 10:
        return False

    if isbn.count("X") == 1:
        if isbn[-1] != "X":
            return False

    if isbn.count("X") > 1:
        return False

    isbn = isbn.split("-")
    isbn_array = []
    for x in isbn:
        for y in x:
            if y == "X":
                isbn_array.append(10)
            else:
                try:
                    isbn_array.append(int(y))
                except ValueError:
                    return False

    total = 0
    for index, num in enumerate(isbn_array):
        total += num * (10 - index)
    return total % 11 == 0
