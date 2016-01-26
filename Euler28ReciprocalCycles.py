dictionary = {}
numbers = list()
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 57, 59, 61,
            67, 71, 73, 79, 83, 87, 89, 91, 97,
            ]
for p in primes:
    dictionary.update({p : 1/p})
    print({p: 1/p})
print(dictionary)

for key, value in dictionary:
    print(key, str(value))
