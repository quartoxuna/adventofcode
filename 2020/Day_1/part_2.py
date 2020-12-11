#!/usr/bin/env python

"""
Your puzzle answer was 445536.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

numbers = []

with open('input.txt') as file_handle:
    numbers = [int(n) for n in file_handle.readlines()]

for first_num in numbers:
    for second_num in numbers:
        for third_num in numbers:
            if first_num + second_num + third_num == 2020:
                print("{} * {} * {} = {}".format(first_num, second_num, third_num, (first_num * second_num * third_num)))

