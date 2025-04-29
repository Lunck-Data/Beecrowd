# 1009 - Salário com Bônus

NOMEDOVAGABUNDO = input()

Salario_fixo = float(input())
Comissao = float(input())

Comissao = Comissao * 0.15

Salario = Salario_fixo + Comissao

print(f"TOTAL = R$ {Salario:.2f}")