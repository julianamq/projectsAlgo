def is_anagram(first_string, second_string):
    sorted_first = ''.join(sorted(first_string.lower()))
    sorted_second = ''.join(sorted(second_string.lower()))
    return sorted_first == sorted_second
