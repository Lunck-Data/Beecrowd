# 1013 - O Maior

dados = input().split()

A = float(dados[0])
B = float(dados[1])
C = float(dados[2])

MaiorAB = (A+B+abs(A-B))/2
MaiorAC = (A+C+abs(A-C))/2

MaiorABC = int((MaiorAB+MaiorAC+abs(MaiorAB-MaiorAC))/2)

print(f"{MaiorABC} eh o maior")