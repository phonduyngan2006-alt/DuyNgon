import math

abs_val = lambda n: abs(n)

add_15 = lambda n: n + 15

multiply = lambda x, y: x * y

is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

area_circle = lambda r: math.pi * r * r if r >= 0 else None

perimeter_rect = lambda d, r: 2 * (d + r) if d > 0 and r > 0 else None

is_perfect_square = lambda n: n >= 0 and int(math.isqrt(n))**2 == n

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

triangle_type = lambda a, b, c: (
    "Không phải tam giác" if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a else
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (a == b and a*a + b*b == c*c) or 
                            (a == c and a*a + c*c == b*b) or 
                            (b == c and b*b + c*c == a*a) else
    "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác thường"
)


n = int(input("Nhập số nguyên n: "))
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

r = float(input("Nhập bán kính r: "))
d = float(input("Nhập chiều dài: "))
w = float(input("Nhập chiều rộng: "))

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

print("\n--- KẾT QUẢ ---")

print("a) |n| =", abs_val(n))
print("b) n + 15 =", add_15(n))
print("c) x * y =", multiply(x, y))

print("d) n có là bội của 13 hoặc 19 không?:", is_multiple_13_19(n))

area = area_circle(r)
print("e) Diện tích hình tròn:", area if area is not None else "Không hợp lệ")

peri = perimeter_rect(d, w)
print("f) Chu vi hình chữ nhật:", peri if peri is not None else "Không hợp lệ")

print("g) n có phải số chính phương không?:", is_perfect_square(n))
print("h) n có phải số nguyên tố không?:", is_prime(n))

print("i) Loại tam giác:", triangle_type(a, b, c))