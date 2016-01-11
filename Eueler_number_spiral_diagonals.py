def top_left(number):
    counter = 0
    for x in range(1, number):
        one_less = x-1
        corner = x**2 - one_less
        counter += corner
    return counter

def bottom_left(number):
    counter = 0
    for x in range(1, number):
        if x % 2 == 0:
            corner = x**2 + 1
        else:
            corner = x**2
        counter += corner
    return counter - 1

print(top_left(1002) + bottom_left(1002))
"""
1   1**2-0 total = 1 + 2*0
3   2**2-1 total = 1 + 1 + 2*1
7   3**2-2 total = 1 + 2*2 + 2*3
13  4**2-3
21  5**2-4
31  6**2-5"""
