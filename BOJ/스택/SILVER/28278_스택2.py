import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == '1':
        stack.append(cmd[1])
    elif cmd[0] == '2':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd[0] == '5':
        if not stack:
            print(-1)
        else:
            print(stack[-1])