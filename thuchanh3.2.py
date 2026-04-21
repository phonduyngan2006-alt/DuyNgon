from datetime import datetime, timedelta

# ======================
# i. Thông tin thời gian hiện tại
# ======================
now = datetime.now()

print("=== THỜI GIAN HIỆN TẠI ===")
print("Năm hiện tại:", now.year)
print("Tháng hiện tại:", now.strftime("%B"))
print("Tuần trong năm:", now.strftime("%U"))
print("Tuần trong tháng:", (now.day - 1) // 7 + 1)
print("Ngày thứ trong năm:", now.strftime("%j"))
print("Ngày hiện tại:", now.day)
print("Thứ:", now.strftime("%A"))
print("Giờ hiện tại:", now.strftime("%H:%M:%S"))

# ======================
# ii. Tính số ngày giữa 2 ngày
# ======================
print("\n=== TÍNH SỐ NGÀY GIỮA 2 NGÀY ===")
d1 = input("Nhập ngày 1 (dd/mm/yyyy): ")
d2 = input("Nhập ngày 2 (dd/mm/yyyy): ")

date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")

diff = abs((date2 - date1).days)
print("Số ngày cách nhau:", diff)

# ======================
# iii. Chuyển chuỗi sang datetime
# ======================
print("\n=== CHUYỂN CHUỖI SANG DATETIME ===")
S = input("Nhập chuỗi (vd: Sep 18 2019 2:43PM): ")

dt = datetime.strptime(S, "%b %d %Y %I:%M%p")
print("Dạng datetime:", dt)

# ======================
# iv. Cộng thêm 5 giây
# ======================
print("\n=== CỘNG THÊM 5 GIÂY ===")
new_time = now + timedelta(seconds=5)

print("Hiện tại:", now.strftime("%H:%M:%S"))
print("Sau 5 giây:", new_time.strftime("%H:%M:%S"))