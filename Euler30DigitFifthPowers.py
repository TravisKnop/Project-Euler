list_of_5th_powers = []
def check_digits(number):
    number_total = 0
    for x in list(str(number)):
        fifth = int(x) ** 5
        number_total += fifth
    if number_total == number:
        list_of_5th_powers.append(number)

for x in range (1000000):
    check_digits(x)

print(sum(list_of_5th_powers[2:]))
