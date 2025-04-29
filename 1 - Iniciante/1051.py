# 1051 - Imposto de Renda

salario = float(input()) # 2900.00

if salario <= 2000.00: #305
    print("Isento")
elif salario >= 2000.01:
    if salario >= 3000.01:
        if salario >= 4500.00:
            imposto = ((salario - 4500) * 0.28) + 350
            print(f"R$ {imposto:.2f}")
        else:
            imposto = ((salario - 3000) * 0.18) + 80
            print(f"R$ {imposto:.2f}")
    else:
        imposto = (salario - 2000) * 0.08
        print(f"R$ {imposto:.2f}")