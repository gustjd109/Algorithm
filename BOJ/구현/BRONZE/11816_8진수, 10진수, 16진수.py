import sys

sys.stdin = open("input.txt","rt")
X = sys.stdin.readline()

if X[0] == '0' and X[1] != 'x':
    print(int(X, 8))
elif X[0] == '0' and X[1] == 'x':
    print(int(X, 16))
else:
    print(X)