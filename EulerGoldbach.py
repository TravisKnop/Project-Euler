import itertools

max_test_number = 10009
max_possible_sqrt = int(max_test_number ** 0.5)
square_roots = list(range(2, max_possible_sqrt + 1))

def get_primes():
    potential_primes = list(range(1, max_test_number + 1))
    for i in square_roots:
        for number in potential_primes:
            if i != number:
                if number % i == 0:
                    potential_primes.remove(number)
    return potential_primes
primes = get_primes()

def get_odd_composites():
    composites = list(range(1, max_test_number + 1))
    for i in primes:
        composites.remove(i)
    composite_odds = []
    for i in composites:
        if i % 2 != 0:
            composite_odds.append(i)
    return composite_odds
composite_odds = get_odd_composites()

print("prime numbers: ", primes)
print("")
print("composite odds: ", composite_odds)

def get_passing_numbers():
    passing_comps = []
    for comp_odd in composite_odds:
        for x, y in itertools.product(primes, square_roots):
            if x + 2 * y**2 == comp_odd:
                passing_comps.append(comp_odd)
    return passing_comps
passing_comps = get_passing_numbers()

for item in composite_odds:
    if item not in passing_comps:
        print("Answer: ", item)
