# 1134 - Tipo de Combustível


def combustivel():
    alcool = 0
    gasolina = 0
    diesel = 0

    while True:

        opcao = int(input())

        if opcao == 1:
            alcool += 1
        
        elif opcao == 2:
            gasolina += 1
        
        elif opcao == 3:
            diesel += 1
        
        elif opcao == 4:
            break

        else:
            continue


    print("MUITO OBRIGADO")
    print(f"Alcool: {alcool}")
    print(f"Gasolina: {gasolina}")
    print(f"Diesel: {diesel}")

combustivel()