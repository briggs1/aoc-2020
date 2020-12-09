text_file = "input.txt"
bad_passports = 0

with open(text_file) as f:
    data = f.read()

data = data.split("\n\n")

req_fields = ["ecl:", "pid:", "eyr:", "hcl:",
              "byr:", "iyr:", "hgt:"]

for line in data:
    for field in req_fields:
        if field not in line:
            bad_passports += 1
            break

print(len(data) - bad_passports)
