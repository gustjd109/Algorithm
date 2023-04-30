import sys

def Factorial(N):
    if N > 0:
        return N * Factorial(N - 1)
    else:
        return 1
    
N = int(sys.stdin.readline())

print(Factorial(N))