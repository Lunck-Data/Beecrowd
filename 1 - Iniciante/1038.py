# 1038 - Lanche

valores = input().split()

codigo = int(valores[0])
quantidade = int(valores[1])
total = 0

if codigo == 1:
    total = quantidade * 4
elif codigo == 2:
    total = quantidade * 4.5
elif codigo == 3:
    total = quantidade * 5
elif codigo == 4:
    total = quantidade * 2
else:
    total = quantidade * 1.5

print(f"Total: R$ {total:.2f}")