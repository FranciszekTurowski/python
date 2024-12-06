def fibonacci(n):
    if n <= 0:
        raise ValueError("n musi być liczbą większą od 0")
    elif n == 1:
        return 0  # Pierwsza liczba Fibonacciego
    elif n == 2:
        return 1  # Druga liczba Fibonacciego

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Przykład użycia:
try:
    n = int(input("Podaj wartość n (n > 0): "))
    print(f"{n}-ta liczba Fibonacciego to: {fibonacci(n)}")
except ValueError as e:
    print(e)
