from itertools import combinations_with_replacement

text_file = "day9/input.txt"
numbers = []
n = 2
begin = 0
end = 25

with open(text_file) as f:
    data = f.read().split("\n")

numbers = list(map(int, data))


while end < len(numbers):
    preamble = numbers[begin:end]
    possible_sums = set(sum(comb)
                        for comb in combinations_with_replacement(preamble, n))
    message = numbers[25:]

    if message[begin] not in possible_sums:
        print(message[begin])

    begin += 1
    end += 1
