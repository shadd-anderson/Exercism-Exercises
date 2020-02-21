def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of the same length")
    else:
        total = 0
        for index, letter in enumerate(strand_a):
            if strand_b[index] != letter:
                total += 1
        return total
