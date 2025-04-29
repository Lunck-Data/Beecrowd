# 1050 - DDD

valor = int(input())

DDD = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"}

def ddd():
    for i in DDD:
        if valor == i:
            print(DDD[i])
            return

    print("DDD nao cadastrado")

ddd()