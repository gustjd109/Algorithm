# 처음 풀이는 큐의 길이를 2로 나누어서 나온 인덱스 값의 큐 값과 그 인덱스 - 1의 값의 큐 값과 비교하여 중간값을 출력하는 방식으로 접근했지만 실패
# import sys
# import heapq

# N = int(sys.stdin.readline())
# Q = []

# for i in range(N):
#     num = int(sys.stdin.readline())
#     heapq.heappush(Q, num)

#     if len(Q) % 2 == 0:
#         if Q[len(Q) // 2] > Q[(len(Q) // 2) - 1]:
#             print(Q[len(Q) // 2])
#     else :
#         print(print(Q[len(Q) // 2]))

########################################################################################################################

# heapq를 이용한 풀이
# 다른분들의 풀이를 보고 풀이한 것으로, 
# 왼쪽 힙(최대 힙)과 오른쪽 힙(최소 힙)을 만들어서 루트를 비교하여 출력하는 방식이다.
# import sys
# import heapq

# N = int(sys.stdin.readline())
# max_heap = []
# min_heap = []

# for _ in range(N):
#     num = int(sys.stdin.readline())

#     # 왼쪽 힙의 길이와 오른쪽 힙의 길이가 같으면
#     if (len(max_heap) == len(min_heap)):
#         # 왼쪽 힙에 숫자의 음수 삽입
#         heapq.heappush(max_heap, -num)
#         # 왼쪽 힙의 길이와 오른쪽 힙의 길이가 다르면
#     else:
#         # 오른쪽 힙에 숫자 삽입
#         heapq.heappush(min_heap, num)

#     # 양쪽 힙에 요소들이 존재하고, 왼쪽 힙의 루트 값에 음수를 곱한 값이 오른쪽 힙의 루트 값보다 크면
#     if len(max_heap) >= 1 and len(min_heap) >= 1 and -max_heap[0] > min_heap[0]:
#         # 왼쪽 힙의 루트 값 삭제
#         max_root = heapq.heappop(max_heap)
#         # 삭제한 왼쪽 힙의 루트 값의 음수 값을 오른쪽 힙에 삽입
#         heapq.heappush(min_heap, -max_root)
#         # 오른쪽 힙의 루트 값 삭제
#         min_root = heapq.heappop(min_heap)
#         # 삭제한 오른쪽 힙의 루트 값의 음수 값을 왼쪽 힙에 삽입
#         heapq.heappush(max_heap, -min_root)

#     # 왼쪽 힙의 루트 값에 음수를 곱한 값 출력
#     print(-max_heap[0])

########################################################################################################################

# 힙 정렬 직접 구현을 통한 풀이
import sys

def up_max_heapify(X):
    n = len(X)

    start = n - 1
    tmp = X[start]
    child = start

    while child > 0:
        parent = (child - 1) // 2

        if tmp <= X[parent]:
            break
        else:
            X[child] = X[parent]
            child = parent
    X[child] = tmp

def up_min_heapify(X):
    n = len(X)

    start = n - 1
    tmp = X[start]
    child = start

    while child > 0:
        parent = (child - 1) // 2

        if tmp >= X[parent]:
            break
        else:
            X[child] = X[parent]
            child = parent
    X[child] = tmp

def down_max_heapify(X):
    n = len(X)

    start = 0
    tmp = X[start]
    parent = start

    while parent < n // 2:
        left_child = (parent * 2) + 1
        right_child = left_child + 1

        if n > right_child:
            a = X[left_child]
            b = X[right_child]
            if a >= b:
                real_child = left_child
            else:
                real_child = right_child
        
        if right_child > n - 1:
            real_child = left_child
        else:
            real_child = right_child if X[right_child] > X[left_child] else left_child

        if tmp >= X[real_child]:
            break
        else:
            X[parent] = X[real_child]
            parent = real_child
    X[parent] = tmp

    
def down_min_heapify(X):
    n = len(X)

    start = 0
    tmp = X[start]
    parent = start

    while parent < n // 2:
        left_child = (parent * 2) + 1
        right_child = left_child + 1

        if n > right_child:
            a = X[left_child]
            b = X[right_child]
            if a >= b:
                real_child = right_child
            else:
                real_child = left_child

        if right_child > n - 1:
            real_child = left_child
        else:
            real_child = right_child if X[right_child] < X[left_child] else left_child

        if tmp <= X[real_child]:
            break
        else:
            X[parent] = X[real_child]
            parent = real_child
    X[parent] = tmp

N = int(sys.stdin.readline())
left_heap = []
right_heap = []

for i in range(N):
    X = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        left_heap.append(X)
        up_max_heapify(left_heap)
    else:
        right_heap.append(X)
        up_min_heapify(right_heap)

    if len(right_heap) != 0 and left_heap[0] > right_heap[0]:
        left_heap[0], right_heap[0] = right_heap[0], left_heap[0]
        down_max_heapify(left_heap)
        down_min_heapify(right_heap)

    print(left_heap[0])