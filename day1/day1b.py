import itertools
import operator
import functools

text_file = "input.txt"
year_number = 2020

with open(text_file) as f:
    number_list = f.read().splitlines()

for subset in itertools.combinations(number_list, 3):
    b = sum(int(i) for i in subset)
    if b == year_number:
        print(int(subset[0]) * int(subset[1]) * int(subset[2]))
