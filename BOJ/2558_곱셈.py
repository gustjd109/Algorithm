A = int(input())
B = int(input())
print(A * (B % 10), A * (B // 10 % 10), A * (B // 100), A * B, sep='\n')