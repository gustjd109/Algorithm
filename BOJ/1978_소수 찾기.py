import sys

N = int(input())
Data = list(map(int, sys.stdin.readline().split()))
Cnt = 0

for i in Data:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                Cnt += 1
            break

print(Cnt)

# import sys

# def FindSosu(Data):
#     if Data == 1:
#         return 0
#     for i in range(2, Data):
#         if Data % i == 0:
#             return 0
#     return 1

# N = int(input())
# Data = list(map(int, sys.stdin.readline().split()))
# Cnt = 0

# for i in range(len(Data)):
#     Cnt += FindSosu(Data[i])

# print(Cnt)