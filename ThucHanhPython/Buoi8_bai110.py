s = input().strip()

result = ""
i = 0

while i < len(s):
    if s[i] == '#':
        count = int(s[i + 1])
        ch = s[i + 2]
        result += ch * count
        i += 3
    else:
        result += s[i]
        i += 1

print(result)