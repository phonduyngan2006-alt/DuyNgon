def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = []

while True:
    try:
        n = int(input("Nhập số nguyên: "))
        numbers.append(n)
    except:
        print("Vui lòng nhập số nguyên hợp lệ!")
        continue

    choice = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().upper()
    if choice == 'N':
        break

# a) In ra các số nguyên tố
primes = [x for x in numbers if is_prime(x)]
print("Các số nguyên tố:", primes)

# b) Trung bình số âm và số dương
negatives = [x for x in numbers if x < 0]
positives = [x for x in numbers if x > 0]

if negatives:
    avg_neg = sum(negatives) / len(negatives)
else:
    avg_neg = 0

if positives:
    avg_pos = sum(positives) / len(positives)
else:
    avg_pos = 0

print("Trung bình số âm:", avg_neg)
print("Trung bình số dương:", avg_pos)

# c) Số lớn nhất, nhỏ nhất
print("Số lớn nhất:", max(numbers))
print("Số nhỏ nhất:", min(numbers))

# d) Kiểm tra tăng dần
is_increasing = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))

if is_increasing:
    print("Danh sách đã được sắp xếp tăng dần.")
else:
    print("Danh sách chưa được sắp xếp tăng dần.")