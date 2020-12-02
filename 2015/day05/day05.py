with open('input.txt') as f:
    strings = [string.strip() for string in f.readlines()]


def three_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiou':
            count += 1
    return count >= 3


def double_letter(string):
    for i, letter in enumerate(string):
        if i < len(string) - 1:
            if letter == string[i + 1]:
                return True
    return False


def double_letter_with_gap(string):
    for i, letter in enumerate(string):
        if i < len(string) - 2:
            if letter == string[i + 2]:
                return True
    return False


def pairs_twice(string):
    for i, letter in enumerate(string):
        if i < len(string) - 3:
            if string[i:i + 2] in string[i + 2:]:
                return True
    return False


def no_bad_string(string):
    no_bad = True
    for pair in ['ab', 'cd', 'pq', 'xy']:
        if pair in string:
            no_bad = False
    return no_bad


# print(strings)
# print('ab' in 'abcdefg')
# print('ab' in 'ajva89ab')
# print('ab' in 'akjaic')
#
# print(no_bad_string('abcdefg'))
# print(no_bad_string('cedfpqg'))
# print(no_bad_string('akjbefg'))
#
# print(double_letter('asfbaf'))
# print(double_letter('asfbbf'))

# part 1
count_good_strings = 0
for string in strings:
    if all([three_vowels(string), double_letter(string), no_bad_string(string)]):
        count_good_strings += 1
print(count_good_strings)

# part 2
# strings = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
# good, good, bad, bad
count_good_strings = 0
for string in strings:
    if all([double_letter_with_gap(string), pairs_twice(string)]):
        count_good_strings += 1
print(count_good_strings)
