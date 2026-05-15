import math

a, b = map(int, input().split())

count = 0

for n in range(a, b + 1):
    rev = int(str(n)[::-1])

    if math.gcd(n, rev) == 1:
        print(n, end=" ")
        count += 1

print()
print(count)