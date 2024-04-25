"""Exercise Description

In English, ordinal numerals have suffixes such as the “th” in “30th” or “nd” in “2nd”. Write an ordinalSuffix() function with an integer parameter named number and returns a string of the number with its ordinal suffix. For example, ordinalSuffix(42) should return the string '42nd'.

You may use Python’s str() function to convert the integer argument to a string. Python’s endswith() string method could be useful for this exercise, but to maintain the challenge in this exercise, don’t use it as part of your solution.

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'

Prerequisite concepts: strings, in operator, slices, string concatenation
"""


def ordinal_suffix_using_str(number: int) -> str:
    """Generate a Ordinal Suffix using str()

    Args:
        number (int): Number to add suffix

    Returns:
        str: Number with Ordinal Suffix
    """
    string: str = str(number)
    suffix: str = ""
    if string[-2:] in ("11", "12", "13"):
        suffix = "th"
    elif string[-1:] == "1":
        suffix = "st"
    elif string[-1:] == "2":
        suffix = "nd"
    elif string[-1:] == "3":
        suffix = "rd"
    else:
        suffix = "th"
    return f"{string}{suffix}"


def ordinal_suffix_using_modulo(number: int) -> str:
    suffix: str = ""
    if number % 100 in (11,12,13):
        suffix = "th"
    elif number % 10 == 1:
        suffix = "st"
    elif number % 10 == 2:
        suffix = "nd"
    elif number % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{number}{suffix}"


def ordinal_suffix(number: int) -> str:
    return ordinal_suffix_using_modulo(number)


assert ordinal_suffix(0) == "0th"

assert ordinal_suffix(1) == "1st"

assert ordinal_suffix(2) == "2nd"

assert ordinal_suffix(3) == "3rd"

assert ordinal_suffix(4) == "4th"

assert ordinal_suffix(10) == "10th"

assert ordinal_suffix(11) == "11th"

assert ordinal_suffix(12) == "12th"

assert ordinal_suffix(13) == "13th"

assert ordinal_suffix(14) == "14th"

assert ordinal_suffix(101) == "101st"
