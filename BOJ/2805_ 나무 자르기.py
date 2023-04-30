import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(N_list)
retult = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in N_list:
        if i > mid:
            cnt += (i - mid)
            if cnt > M:
                break
    if cnt > M:
        start = mid + 1
        result = mid # 자른 나무들의 총합인 cnt값이 가져가려는 나무 길이보다 클때에도 mid값을 결과값에 넣어줘야 함
    elif cnt == M:
        result = mid
        break
    else:
        end = mid - 1

print(result)

# 제일 처음에 풀었던 코드 -> 시간초과 -> pypy로 돌리면 통과 -> 서버 ㅂㅅ
import sys
N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(N_list)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in N_list:
        if i > mid:
            cnt += (i - mid)
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)