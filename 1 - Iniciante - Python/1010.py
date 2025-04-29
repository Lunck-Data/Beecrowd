# 1010 - Cálculo Simples 

Peças1 = input().split()
Peças2 = input().split()

codigo1 = int(Peças1[0])
codigo2 = int(Peças2[0])

unid1 = int(Peças1[1])
unid2 = int(Peças2[1])

preco1 = float(Peças1[2])
preco2 = float(Peças2[2])

total1 = unid1 * preco1
total2 = unid2 * preco2

TOTAL = total1 + total2

print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")