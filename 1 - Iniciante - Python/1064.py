# 1064 - Positivos e Média

lista = []

for A in range(0, 6):
    B = float(input())
    lista.append(B)

listaPositivos = []
contador = 0
total = 0

for A in lista:
    if A > 0:
        listaPositivos.append(A)
        contador += 1
        total = total + A
        
print(f"{contador} valores positivos")
print(f"{total/contador:.1f}")