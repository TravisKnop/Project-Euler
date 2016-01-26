palindromic_numbers = []
products_of_two_three_digit_numbers = []

def get_largest_palindromes():
    for x in range(100*100, 999*999):
        if str(x) == str(x)[::-1]:
            palindromic_numbers.append(x)
    return palindromic_numbers[::-1]

def get_three_digit_products():
    x = sorted(range(100,1000))[:500:-1]
    y = sorted(range(100,1000))[:500:-1]
    for first in x:
        for second in y:
            products_of_two_three_digit_numbers.append(first*second)
    return sorted(products_of_two_three_digit_numbers)[::-1]

def cross_check_3_digit_products_and_palindromes():
    for x in get_three_digit_products():
        if x in palindromic_numbers:
            print("We have a winner! {}".format(x))
            break

get_largest_palindromes()
get_three_digit_products()
cross_check_3_digit_products_and_palindromes()
