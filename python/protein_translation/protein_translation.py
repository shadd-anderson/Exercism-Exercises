proteins_from_codons = {"AUG": "Methionine",
                        "UUU": "Phenylalanine",
                        "UUC": "Phenylalanine",
                        "UUA": "Leucine",
                        "UUG": "Leucine",
                        "UCU": "Serine",
                        "UCC": "Serine",
                        "UCA": "Serine",
                        "UCG": "Serine",
                        "AGU": "Serine",
                        "UAU": "Tyrosine",
                        "UAC": "Tyrosine",
                        "UGU": "Cysteine",
                        "UGC": "Cysteine",
                        "UGG": "Tryptophan",
                        "CAG": "Glutamine",
                        "GUC": "Valine"}


def proteins(strand):
    protein_strand = []
    i = 0
    while i < len(strand):
        codon = strand[i:i+3]
        if codon in {"UAA", "UAG", "UGA"}:
            return protein_strand
        elif len(codon) == 3:
            protein_strand.append(proteins_from_codons[codon])
        i += 3
    return protein_strand
