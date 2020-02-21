def convert(number):
    final = ""
    if number % 3 == 0:
        final += "Pling"

    if number % 5 == 0:
        final += "Plang"

    if number % 7 == 0:
        final += "Plong"

    if final == "":
        return str(number)
    else:
        return final
