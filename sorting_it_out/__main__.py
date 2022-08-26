import string


def sorting_it_out(value: str, case_sensitive: bool = False) -> str:
    character_map = build_character_map(value, case_sensitive)
    return build_result_string(character_map, case_sensitive)


def build_character_map(value: str, case_sensitive: bool) -> dict:
    filtered_string = filter_non_alphabet_characters(value)
    character_map = {}
    for character in filtered_string:
        key = character if case_sensitive else character.lower()
        character_map[key] = 1 if key not in character_map else character_map[key] + 1
    return character_map
    
    
def filter_non_alphabet_characters(value: str) -> str:
    return ''.join(filter(str.isalpha, value))


def build_result_string(character_map: dict, case_sensitive: bool) -> str:
    result = ""
    keys = string.ascii_letters if case_sensitive else string.ascii_lowercase
    for key in keys:
        if key in character_map:
            result += key * character_map[key]
    return result
