def slices(series, length):
    if 0 >= length or length > len(series):
        raise ValueError("That is not a valid request! Length must be greater than zero \n"
                         "and less than the length of the series")
    else:
        final = []
        start, end = 0, length
        while end < len(series) + 1:
            final.append(series[start:end])
            start, end = start + 1, end + 1
        return final
