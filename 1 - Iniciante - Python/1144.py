# 1144 - Sequência Lógica

valor = int(input())

lista = list(range(1,(valor+1)))
lista.sort()

for i in lista:

    A = i ** 2
    B = i * A
    print(f"{i} {A} {B}") 
    print(f"{i} {A+1} {B+1}") 