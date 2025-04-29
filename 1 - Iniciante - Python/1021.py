# 1021 - Notas e Moedas

valor = float(input())

valor_inicio = valor

notas100 = valor // 100
valor = valor % 100
notas50 = valor // 50
valor = valor % 50
notas20 = valor // 20
valor = valor % 20
notas10 = valor // 10
valor = valor % 10
notas5 = valor // 5
valor = valor % 5
notas2 = valor // 2
valor = valor % 2

moeda1 = valor // 1
valor = valor % 1
moeda05 = valor // 0.5
valor = valor % 0.5
moeda025 = valor // 0.25
valor = valor % 0.25
moeda010 = valor // 0.10
valor = valor % 0.10
moeda005 = valor // 0.05
valor = valor % 0.05
moeda001 = valor / 0.01


print("NOTAS:")
print(f"{notas100:.0f} nota(s) de R$ 100.00")
print(f"{notas50:.0f} nota(s) de R$ 50.00")
print(f"{notas20:.0f} nota(s) de R$ 20.00")
print(f"{notas10:.0f} nota(s) de R$ 10.00")
print(f"{notas5:.0f} nota(s) de R$ 5.00")
print(f"{notas2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1:.0f} moeda(s) de R$ 1.00")
print(f"{moeda05:.0f} moeda(s) de R$ 0.50")
print(f"{moeda025:.0f} moeda(s) de R$ 0.25")
print(f"{moeda010:.0f} moeda(s) de R$ 0.10")
print(f"{moeda005:.0f} moeda(s) de R$ 0.05")
print(f"{moeda001:.0f} moeda(s) de R$ 0.01")