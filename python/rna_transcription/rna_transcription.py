dnatorna = {"G": "C",
            "C": "G",
            "T": "A",
            "A": "U"}


def to_rna(dna_strand):
    rna_strand = ""
    for letter in dna_strand:
        rna_strand += dnatorna[letter]
    return rna_strand
