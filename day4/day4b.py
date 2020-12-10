import re


def eye_color_check(s):
    if len(s) == 3 and s in eye_colors:
        return True


def birth_year_check(s):
    year = int(s)
    if len(s) == 4 and year >= 1920 and year <= 2002:
        return True
    else:
        return False


def issue_year_check(s):
    year = int(s)
    if len(s) == 4 and year >= 2010 and year <= 2020:
        return True
    else:
        return False


def expiration_year_check(s):
    year = int(s)
    if len(s) == 4 and year >= 2020 and year <= 2030:
        return True
    else:
        return False


def height_check(s):
    height = int(''.join(filter(lambda i: i.isdigit(), s)))
    if "cm" in s and height >= 150 and height <= 190:
        return True
    elif "in" in s and height >= 59 and height <= 76:
        return True
    else:
        return False


def hair_color_check(s):
    return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', s)


def passport_id_check(s):
    return re.search(r'(\d{9})', s)


valid = True

text_file = "input.txt"
bad_passports = 0
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


with open(text_file) as f:
    data = f.read().split("\n\n")

req_fields = ["ecl", "pid", "eyr", "hcl",
              "byr", "iyr", "hgt"]

def_map = {"ecl": eye_color_check, "pid": passport_id_check, "eyr": expiration_year_check,
           "hcl": hair_color_check, "byr": birth_year_check, "iyr": issue_year_check, "hgt": height_check}

for line in data:
    d = dict(re.findall(r'(\S+):(".*?"|\S+)', line))

    for field in req_fields:
        valid = True
        if field not in d.keys():
            bad_passports += 1
            valid = False
            break

        for key, value in d.items():
            if key in def_map:
                valid = def_map[key](value)

            if valid == False:
                bad_passports += 1
                break

print(bad_passports)
print(len(data) - bad_passports)
