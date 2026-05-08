
S = input("Nhập số điện thoại: ")

khong_xuat_hien = []

for i in range(10):
    if str(i) not in S:
        khong_xuat_hien.append(i)

print("Các chữ số không xuất hiện:", khong_xuat_hien)


S = input("\nNhập chuỗi: ")

ds_tu = S.split()

da_gap = set()
ket_qua = None

for tu in ds_tu:
    if tu in da_gap:
        ket_qua = tu
        break
    da_gap.add(tu)

print("Từ đầu tiên lặp lại:", ket_qua)