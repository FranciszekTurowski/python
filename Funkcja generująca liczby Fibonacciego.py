# Funkcja generująca liczby Fibonacciego
def generate_fibonacci(limit):
    fibonacci_numbers = []
    a, b = 0, 1
    while a <= limit:
        fibonacci_numbers.append(a)
        a, b = b, a + b
    return fibonacci_numbers

# Ustawienie limitu
limit = 1000

# Generowanie liczb Fibonacciego
fibonacci_numbers = generate_fibonacci(limit)

# Zapis do pliku tekstowego
with open('fibonacci_numbers.txt', 'w') as file:
    for number in fibonacci_numbers:
        file.write(f"{number}\n")

print("Liczby Fibonacciego zostały zapisane w pliku 'fibonacci_numbers.txt'.")
