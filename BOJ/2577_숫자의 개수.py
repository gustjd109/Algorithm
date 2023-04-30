A = int(input())
B = int(input())
C = int(input())

mul = list(str(A * B * C))
for i in range(0, 10):
    cnt = 0
    for j in mul:
        if i == int(j):
            cnt += 1
    print(cnt)

# A = int(input())
# B = int(input())
# C = int(input())

# mul = list(str(A * B * C))

# for i in range(10):
#     print(mul.count(str(i)))