#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	n = ((number * -1) % 10) * -1)
else:
	n = number % 10

if n > 5:
	phrase = "and is greater than 5"
elif n == 0:
	phrase = "and is 0"
elif n < 6 and number != 0:
	phrase = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, n, phrase))
