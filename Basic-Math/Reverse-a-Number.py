x = 123
arr = []

while x > 0:
    arr.append(x % 10)
    x = x // 10

res = 0
for i in arr:
    res.append(i)

print(res)