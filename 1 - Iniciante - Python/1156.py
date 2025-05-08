# 1156 - Sequência S II

S = 1

A = 1
B = 1

for i in range(1, 20):
    A = A + 2
    B = B * 2
    S = S + (A/B)

print(f"{S:.2f}")