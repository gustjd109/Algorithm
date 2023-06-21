import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    K = int(sys.stdin.readline())
    if K == 0:
        stack.pop()
    else:
        stack.append(K)
sum_stack_val = sum(stack)

print(sum_stack_val)