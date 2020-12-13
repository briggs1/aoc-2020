text_file = "input.txt"
count = 0

with open(text_file) as f:
    data = f.read().split("\n\n")

for line in data:
    group = line.split("\n")
    used_answers = []
    for member in group:
        for char in member:
            if char not in used_answers:
                count = count + 1
                used_answers.append(char)

print(count)
