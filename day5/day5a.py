text_file = "input.txt"
rows = []
columns = [i for i in range(8)]
seat_ids = []

with open(text_file) as f:
    data = f.read().split("\n")

for line in data:
    rows = [i for i in range(128)]
    for char in line[0:7]:

        half = len(rows)//2

        if char == "B":
            rows = rows[half:]
        elif char == "F":
            rows = rows[:half]

    for char in line[:3]:

        half = len(columns)/2

        if char == "R":
            columns = columns[half:]
        elif char == "L":
            columns = columns[:half]

    seat_ids = seat_ids + [rows[0] * 8 + columns[0]]

print(max(seat_ids))
