"""
Exercise Description

Write a convertToFahrenheit() function with a degreesCelsius parameter. This function returns the number of this temperature in degrees Fahrenheit. Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius.

Use these two formulas for converting between Celsius and Fahrenheit:

·       Fahrenheit = Celsius × (9 / 5) + 32

·       Celsius = (Fahrenheit - 32) × (5 / 9)

These Python assert statements stop the program if their condition is False. Copy them to the bottom of your solution program. Your solution is correct if the following assert statements’ conditions are all True:

assert convert_to_celsius(0) == -17.77777777777778

assert convert_to_celsius(180) == 82.22222222222223

assert convert_to_fahrenheit(0) == 32

assert convert_to_fahrenheit(100) == 212

assert convert_to_celsius(convertToFahrenheit(15)) == 15

# Rounding errors cause a slight discrepancy:

assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001

Prerequisite concepts: math operators
"""

# TODO Convert to OOP


def convert_to_fahrenheit(degreesCelsius):
    """Converts degrees in Celsius to Fahrenheit

    Args:
        degreesFahrenheit (Any): Degrees in Celsius to convert

    Returns:
        float: Temperature in Fahrenheit
    """
    # Fahrenheit = Celsius × (9 / 5) + 32
    return degreesCelsius * (9 / 5) + 32


def convert_to_celsius(degreesFahrenheit):
    """Converts degrees in Fahrenheit to Celsius

    Args:
        degreesFahrenheit (Any): Degrees in Fahrenheit to convert

    Returns:
        float: Temperature in Celsius
    """
    # Celsius = (Fahrenheit - 32) × (5 / 9)
    return (degreesFahrenheit - 32) * (5 / 9)


assert convert_to_celsius(0) == -17.77777777777778

assert convert_to_celsius(180) == 82.22222222222223

assert convert_to_fahrenheit(0) == 32

assert convert_to_fahrenheit(100) == 212

assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
