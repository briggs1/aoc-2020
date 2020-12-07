text_file = "day2/input.txt"
valid_password_count = 0

with open(text_file) as f:
    password_list = f.read().splitlines()

for rule_and_password in password_list:
    word_bits = rule_and_password.split(" ")
    minumum = int(word_bits[0].split("-")[0])
    maximum = int(word_bits[0].split("-")[1])
    letter = word_bits[1][0]
    password = word_bits[2]
    num_letter_in_password = password.count(letter)

    if num_letter_in_password >= minumum and num_letter_in_password <= maximum:
        valid_password_count += 1

print(valid_password_count)
