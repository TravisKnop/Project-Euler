array = range(101)

def sum_squares(array):
    sum_sq = []
    for x in array:
        sum_sq.append(x**2)
    return sum(sum_sq)

def square_sum(array):
    return sum(array) ** 2

print(sum_squares(array))
print(square_sum(array))
print(square_sum(array) - sum_squares(array))
