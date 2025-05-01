# Experiências - 1094

valor = int(input())

total = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(0, valor):
    cobaia = input().split()
    quantidade = int(cobaia[0])
    animal = cobaia[1]

    total = total + quantidade

    if animal == "C":
        coelhos = coelhos + quantidade
    elif animal == "R":
        ratos = ratos + quantidade
    else:
        sapos = sapos + quantidade


print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos/total*100):.2f} %")
print(f"Percentual de ratos: {(ratos/total*100):.2f} %")
print(f"Percentual de sapos: {(sapos/total*100):.2f} %")