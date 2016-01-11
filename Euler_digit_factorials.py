def factorial(number):
    counter = 1
    for x in range(1, number+1):
        counter *= x
    return counter

def curious(number):
    string_num = str(number)
    count = 0
    for x in string_num:
        count += factorial(int(x))
        if count == number:
            print(number)

"""for i in range(1000000):
    curious(i)
"""
for x in range(0, 10):
    print(factorial(x))
