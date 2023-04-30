MaxNum = 0
MaxNumIndex = 0

for i in range(9):
    N = int(input())

    if N > MaxNum:
        MaxNum = N
        MaxNumIndex = i + 1

print(MaxNum, MaxNumIndex, sep='\n')