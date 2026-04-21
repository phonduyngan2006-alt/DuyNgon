#greeting
# Nhập dữ liệu
S = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

# Chuẩn hóa chuỗi (viết thường)
S = S.lower()
word = word.lower()

# Tách từ
words = S.split()

# Đếm số lần xuất hiện
count = words.count(word)

# In kết quả
print(f"Số từ '{word}' là:", count)