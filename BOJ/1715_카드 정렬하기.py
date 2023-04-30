# 비교 횟수가 가장 작으려면 가장 작은 값들부터 먼저 계산해야 한다.
# 단 하나의 값이 남을 때까지 가장 작은 값 2개를 계산한다.
# 계산한 값을 추가하고 저장하는 것을 반복한다.

import sys, heapq

N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for i in range(N)]
heapq.heapify(cards)
cnt = 0

while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    cnt += tmp

print(cnt)