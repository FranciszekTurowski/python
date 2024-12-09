def fibonacci_sequence(n):
    if n <= 0:
        raise ValueError("n musi być liczbą większą od 0")
    
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Przykład użycia:
try:
    n = int(input("Podaj liczbę n (n > 0): "))
    wynik = fibonacci_sequence(n)
    print(f"Pierwsze {n} liczb ciągu Fibonacciego: {wynik}")
except ValueError as e:
    print(e)
