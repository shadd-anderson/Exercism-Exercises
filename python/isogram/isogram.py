import re


def is_isogram(string):
    processed_string = "".join(re.findall("\w*", string.lower()))
    return len(set(processed_string)) == len(processed_string)
