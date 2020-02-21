def find_anagrams(word, candidates):
    anagrams = []
    word = word.lower()
    for candidate in candidates:
        lower_candidate = candidate.lower()
        if word == lower_candidate:
            continue
        else:
            if sorted(word) == sorted(lower_candidate):
                anagrams.append(candidate)
    return anagrams
