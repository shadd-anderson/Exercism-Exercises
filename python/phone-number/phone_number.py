import re


gen_error = ValueError("Final number must be 10 digits long and start with 2-9")


class PhoneNumber:
    def __init__(self, number):
        number = re.sub(r"[^\d]+", "", number)
        if len(number) == 11:
            if number[0] != "1":
                raise ValueError("Country code must be 1")
            else:
                number = number[1:]

        if len(number) == 10:
            if number[0] in ["0", "1"] or number[3] in ["0", "1"]:
                raise gen_error
            else:
                self.number = number
                self.area_code = number[:3]
        else:
            raise gen_error

    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:10]}"
