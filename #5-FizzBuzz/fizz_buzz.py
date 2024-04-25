"""Fizz buzz is a word game you can implement as a simple program. It became famous as a screening question in coding interviews to quickly determine if candidates had any programming ability whatsoever, so being able to solve it quickly leads to a good first impression.

This exercise continues our use of the modulo operator to determine if numbers are divisible by 3, 5, or both 3 and 5. “Divisible by n” means that it can be divided by a number n with no remainder. For example, 10 is divisible by 5, but 11 is not divisible by 5.

Exercise Description

Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1 up to and including upTo, the function prints one of four things:

·       Prints 'FizzBuzz' if the number is divisible by 3 and 5.

·       Prints 'Fizz' if the number is only divisible by 3.

·       Prints 'Buzz' if the number is only divisible by 5.

·       Prints the number if the number is neither divisible by 3 nor 5.

Instead of printing each string or number on a separate line, print them without newlines. For example, your solution is correct if calling fizzBuzz(35) produces the following output:

1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz

Try to write a solution based on the information in this description. If you still have trouble solving this exercise, read the Solution Design and Special Cases and Gotchas sections for additional hints.

Prerequisite concepts: modulo operator, end keyword argument for print(), for loops, range() with two arguments
"""


def fizz_buzz(upTo: int):
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


fizz_buzz(1500)
