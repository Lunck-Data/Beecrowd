# 1176 - Fibonacci em Vetor

T = int(input())

fibonacci = [0, 1, 1]
penultimo = 1
ultimo = 1

for i in range (1, 100):
    atual = ultimo + penultimo
    fibonacci.append(atual)
    penultimo = ultimo
    ultimo = atual

for i in range(0, T):
    X = int(input())
    print(f"Fib({X}) = {fibonacci[X]}")