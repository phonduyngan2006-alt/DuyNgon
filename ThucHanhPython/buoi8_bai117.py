n = input().strip()

S = 0
length = len(n)

for i in range(length):
    for j in range(i + 1, length + 1):
        sub = int(n[i:j])
        S += sub ** 2

print(S)