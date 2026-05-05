from collections import Counter

S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

c1 = Counter(S1)
c2 = Counter(S2)

common = c1 & c2  
print("a) Ký tự chung:", list(common.keys()))

only_s1 = set(S1) - set(S2)
only_s2 = set(S2) - set(S1)

print("b) Số ký tự chỉ có trong S1:", len(only_s1))
print("   Số ký tự chỉ có trong S2:", len(only_s2))

print("c) Ký tự có trong S1 nhưng không có trong S2:", list(only_s1))
print("   Ký tự có trong S2 nhưng không có trong S1:", list(only_s2))