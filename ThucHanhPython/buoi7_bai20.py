menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhap so tien X: "))

tong_to = 0
tong_loai = 0

print(f"So tien {x} duoc doi thanh:")

for tien in menh_gia:
    so_to = 0

    while x >= tien:
        x = x - tien
        so_to += 1

    # Chỉ in khi số tờ > 0
    if so_to > 0:
        print(f"Loai {tien} gom {so_to} to")

        tong_to += so_to
        tong_loai += 1

print(f"TONG CONG CO {tong_to} TO")
print(f"Tong so loai = {tong_loai}")