#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0

    roman_numbers = {
                    "I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000
                    }

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    nums = [roman_numbers[i] for i in roman_string]

    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            nums[i + 1] -= nums[i]
        else:
            total += nums[i]
    total += nums[len(nums) - 1]

    return total
