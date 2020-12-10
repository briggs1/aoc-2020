text_file = "input.txt"
total_trees = 0
i = 0

with open(text_file) as f:
    data = f.read()

data = data.split("\n")

x = 1

while i < len(data):
    pos = (i * x) % len(data[i])
    if data[i][pos] == "#":
        total_trees += 1
    i += 2

print(total_trees)

a = 82 * 173 * 84 * 80 * 35

print(a)
