max_value = 4000000

def generate_fibonacci(max_value):
    sequence = [1, 2]
    while sequence[-1] < max_value:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

fibonacci = generate_fibonacci(max_value)
even_fibonacci = fibonacci[1::3]
print(sum(even_fibonacci))
