import sys

def mixdrink():
    result = drinks[0]
    for i in range(1, N):
        result += (drinks[i] / 2)
    
    if result % 1 > 0:
        print(result)
    else:
        print(int(result))

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    N = int(sys.stdin.readline())
    drinks = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
    mixdrink()