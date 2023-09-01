import sys

N = int(sys.stdin.readline())
result = 0

for _ in range(N):
    word = sys.stdin.readline().strip()
    stack = [word[0]]

    for i in range(1, len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])
    
    if not stack:
        result += 1

print(result)