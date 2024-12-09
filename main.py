def fib_recur(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fib_recur(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Przykład użycia
#Napisz program, który znajdzie n-tą liczbę Fibonacciego dla n > 0.

wyraz = int(input("Podaj wyraz który chcesz obliczyć: "))

print("wynik to:",fib_recur(wyraz))
