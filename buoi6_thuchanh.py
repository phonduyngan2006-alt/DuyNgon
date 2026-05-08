

with open("python.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Nội dung file gốc:")
print(text)


words = text.split()

unique_words = []

positions = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

    positions.append(unique_words.index(word))


with open("compressed.txt", "w", encoding="utf-8") as f:

    # Dòng 1: các từ duy nhất
    f.write(" ".join(unique_words) + "\n")

    # Dòng 2: vị trí xuất hiện
    f.write(" ".join(map(str, positions)))

print("\nĐã tạo file compressed.txt")


with open("compressed.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

unique_words = lines[0].split()
positions = list(map(int, lines[1].split()))



restored_words = []

for pos in positions:
    restored_words.append(unique_words[pos])

restored_text = " ".join(restored_words)


with open("restore.txt", "w", encoding="utf-8") as f:
    f.write(restored_text)

print("Đã tạo file restore.txt")


print("\nVăn bản sau khi khôi phục:")
print(restored_text)