import sys

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    print(binary_search(N_list, i, 0, N - 1))