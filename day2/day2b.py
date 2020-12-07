text_file = "input.txt"
valid_password_count = 0

with open(text_file) as f:
    password_list = f.read().splitlines()

for rule_and_password in password_list:
    word_bits = rule_and_password.split(" ")
    position1 = int(word_bits[0].split("-")[0]) - 1
    position2 = int(word_bits[0].split("-")[1]) - 1
    letter = word_bits[1][0]
    password = word_bits[2]
    num_letter_in_password = password.count(letter)

    if len(password) > position1 and len(password) > position2:
        if password[position1] == letter and password[position2] != letter or password[position1] != letter and password[position2] == letter:
            valid_password_count += 1
    elif len(password) > position1 and len(password) <= position2:
        if password[position1] == letter:
            valid_password_count += 1

print(valid_password_count)
