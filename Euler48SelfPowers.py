my_set = range(1, 1001)
def self_power(x):
    return x ** x
power_set = list(self_power(x) for x in my_set)

print(my_set[-1])
print(str(sum(power_set))[-10:])
