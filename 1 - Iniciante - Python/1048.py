# 1048 - Aumento de Salário

salarioAtual = float(input())

if salarioAtual >= 0 and salarioAtual <= 400.00: #15%
    acrescimo = salarioAtual * 0.15
    salarioNovo = acrescimo + salarioAtual
    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {acrescimo:.2f}")
    print(f"Em percentual: 15 %")
elif salarioAtual >= 400.01 and salarioAtual <= 800.00: #12%
    acrescimo = salarioAtual * 0.12
    salarioNovo = acrescimo + salarioAtual
    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {acrescimo:.2f}")
    print(f"Em percentual: 12 %")
elif salarioAtual >= 800.01 and salarioAtual <= 1200.00: #10%
    acrescimo = salarioAtual * 0.10
    salarioNovo = acrescimo + salarioAtual
    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {acrescimo:.2f}")
    print(f"Em percentual: 10 %")
elif salarioAtual >= 1200.01 and salarioAtual <= 2000.00: #7%
    acrescimo = salarioAtual * 0.07
    salarioNovo = acrescimo + salarioAtual
    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {acrescimo:.2f}")
    print(f"Em percentual: 7 %")
else: #4%
    acrescimo = salarioAtual * 0.04
    salarioNovo = acrescimo + salarioAtual
    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {acrescimo:.2f}")
    print(f"Em percentual: 4 %")