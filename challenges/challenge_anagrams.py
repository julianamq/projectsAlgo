def sorting(string):
    letter_list = list(string.lower())
    exchange = True
    counter = 0
    while exchange:
        exchange = False
        for i in range(len(letter_list) - counter - 1):
            if letter_list[i] > letter_list[i + 1]:
                letter_list[i], letter_list[i + 1] = \
                    letter_list[i + 1], letter_list[i]
                exchange = True
        counter += 1
    return letter_list


def is_anagram(first_string, second_string):
    sorted_first = sorting(first_string)
    sorted_second = sorting(second_string)
    return (
        ''.join(sorted_first),
        ''.join(sorted_second),
        sorted_first == sorted_second
    )
