import string


def sorting_it_out(value: str, case_sensitive: bool = False) -> str:
    cdict = {}
    for char in value:
        if char not in string.ascii_letters:
            continue
        if not case_sensitive:
            char = char.lower()
        cdict[char] = cdict[char] + 1 if char in cdict else 1

    result = ""
    alphabet = string.ascii_letters if case_sensitive else string.ascii_lowercase
    for key in alphabet:
        if key in cdict:
            result += key * cdict[key]
    return result
