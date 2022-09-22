# 跑五圈
count = 1
while count <= 5:
    print(" Run")
    count += 1

# 案例
i = 1
s = 0
while i <= 100:
    s = s + i
    i = i + 1
print(s)

for x in "python":
    print(x)

for x in range(1, 10):
    for y in range(1, x + 1):
        print('{}x{}={}\t'.format(y, x, x * y), end='')
    print()
