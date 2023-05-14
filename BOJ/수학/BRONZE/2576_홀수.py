import sys

sys.stdin = open("input.txt","rt")
odd_num_list = []
for _ in range(7):
    N = int(sys.stdin.readline())
    if N % 2 == 1:
        odd_num_list.append(N)
if not odd_num_list:
    print(-1)
else:
    print(sum(odd_num_list), min(odd_num_list), sep="\n")