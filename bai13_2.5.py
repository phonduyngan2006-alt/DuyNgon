import re

S = input("Nhập chuỗi: ")

# 1. Xóa khoảng trắng đầu/cuối
S = S.strip()

# 2. Chuẩn hóa nhiều space thành 1 space
S = re.sub(r'\s+', ' ', S)

# 3. Xóa khoảng trắng trước dấu , .
S = re.sub(r'\s+([,.])', r'\1', S)

# 4. Đảm bảo sau dấu có 1 khoảng trắng (nếu cần)
S = re.sub(r'([,.])([^\s])', r'\1 \2', S)

print("Chuỗi hoàn chỉnh:")
print(S)