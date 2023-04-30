import sys, heapq

N = int(sys.stdin.readline())
# 입력받은 집과 오피스 좌표 중, 더 값이 작은 것을 기준으로 오름차순 정렬
roads_info = [sorted(list(map(int, sys.stdin.readline(). split()))) for i in range(N)]
# 집과 오피스 좌표를 오른쪽 끝점(도착지) 기준으로 오름차순 정렬
# 철로를 확인할 때, 가장 작은 위치부터 확인하기 위함
roads_info.sort(key=lambda x: x[1])
d = int(sys.stdin.readline())
# 출발점을 저장할 최소힙
heap = []
cnt = 0

for i in roads_info:
    start, end = i
    # 철로 길이보다 짧은 집 또는 오피스만 최소힙에 저장
    if end - start <= d:
        heapq.heappush(heap, start)
        # 최소힙이 비어있지 않고, 선로의 길이보다 큰 집 또는 오피스는 최소힙에서 삭제
        while heap and end - heap[0] > d:
            heapq.heappop(heap)
        # 최대 집 또는 오피스 개수 갱신
        cnt = max(cnt, len(heap))

print(cnt)