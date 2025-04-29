# 1040 - Média 3

notas = input().split()

N1 = round(0.2 * float(notas[0]), 1)
N2 = round(0.3 * float(notas[1]), 1)
N3 = round(0.4 * float(notas[2]), 1)
N4 = round(0.1 * float(notas[3]), 1)

def medias(N1, N2, N3, N4):

    media = N1 + N2 + N3 + N4

    print(f"Media: {media:.1f}")

    if media >= 7.0:
        return print("Aluno aprovado.")
    elif media < 5:
        return print("Aluno reprovado.")

    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    notaMedia = (exame + media) / 2

    if notaMedia >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {notaMedia:.1f}")
    elif notaMedia < 5:
        print("Aluno reprovado.")
        print(f"Media final: {notaMedia:.1f}")

medias(N1, N2, N3, N4)