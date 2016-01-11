import itertools
base = list(range(100))
expo = list(range(30))
digit_power_sums = []

def check_num():
    for x, y in itertools.product(base, expo):
        power = x ** y
        if power >=10:
            list_digits = list(str(power)[0:])
            sum_digits = sum(map(int, list_digits))
            if sum_digits == x:
                digit_power_sums.append(power)

check_num()
print(sorted(digit_power_sums)[29])
