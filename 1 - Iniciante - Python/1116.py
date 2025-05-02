# 1116 - Dividindo X por Y

def divindo():
    valor = int(input())

    for i in range(0 , valor):
        numeros = input().split()
        x = int(numeros[0])
        y = int(numeros[1])
        if y == 0:
            print("divisao impossivel")
            continue
        divisao = x / y
        print(f"{divisao:.1f}")

divindo()