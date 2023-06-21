# 이 문제는 1406번 에디터 문제와 같은 방법을 이용하여 풀 수 있는 문제이다.
# 동일하게 두 개의 스택을 이용해서 각 문제들을 옮겨가면서 풀면 된다.

import sys

sys.stdin = open("input.txt","rt")
T = int(sys.stdin.readline())

for _ in range(T):
    Left = []
    Right = []
    cmd = list(sys.stdin.readline().strip())
    for i in cmd:
        if i == '<':
            if Left:
                Right.append(Left.pop())
        elif i == '>':
            if Right:
                Left.append(Right.pop())
        elif i == '-':
            if Left:
                Left.pop()
        else:
            Left.append(i)
    print(''.join(Left + Right[::-1]))