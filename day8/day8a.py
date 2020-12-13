text_file = "input.txt"
acc = 0
i = 0
used_indices = []

with open(text_file) as f:
    data = f.read().split("\n")

while i < len(data):
    command = data[i]
    old_index = i
    used_indices.append(old_index)

    if command.startswith("acc"):
        acc += int(command.split()[1])
        i += 1
    elif command.startswith("jmp"):
        i = i + int(command.split()[1])
    else:
        i += 1

    if i in used_indices:
        print(acc)
        break
