# 1151 - Fibonacci Fácil

def fibonacci():
    valor = int(input())

    Fibonacci = ['0', '1']

    A = 0
    B = 1

    for i in range(0, (valor-2)):
        atual = A + B
        A = B
        B = atual
        Fibonacci.append(f"{atual}")
    
    Fibonacci = " ".join(Fibonacci)
    return print(Fibonacci)

fibonacci()