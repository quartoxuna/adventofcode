#!/usr/bin/env python

"""
Your puzzle answer was 418.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""

import re

def password_is_valid(password, policy):
    match = re.match(r"(\d+)-(\d+)\s(\w+)", policy)
    assert match, "Invalid policy: '{}'".format(policy)
    positions = [int(match.group(1)), int(match.group(2))]
    char = str(match.group(3))
    chars = [password[i-1] for i in positions]
    return chars.count(char) == 1

valid = 0
with open('input.txt') as file_handle:
    for line in file_handle.readlines():
        # Split password and policy
        policy, password = [x.strip() for x in line.split(':')]
        if password_is_valid(password, policy):
            valid += 1
            print(line)
print("Valid: {}".format(valid))
