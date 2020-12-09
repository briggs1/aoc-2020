text_file = "input.txt"
total_trees = 0
i = 0

with open(text_file) as f:
    data = f.read()

data = data.split("\n")

while i < len(data):
    pos = (i * 3) % len(data[i])
    if data[i][pos] == "#":
        total_trees += 1
    i += 1

print(total_trees)
