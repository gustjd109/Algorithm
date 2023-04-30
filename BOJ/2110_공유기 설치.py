import sys

N, C = map(int, sys.stdin.readline().split())

N_list = []
for _ in range(N):
    N_list.append(int(sys.stdin.readline()))
N_list.sort() # 이진탐색을 위해 집 좌표 리스트 정렬

start = 1 # 집과 집 사이의 최소거리 1로 초기화
end = N_list[-1] - N_list[0] # 집과 집 사이의 최대거리 가장 먼 집과 가장 가까운 집과의 거리로 초기화 

result = 0

while start <= end:
    mid = (start + end) // 2
    value = N_list[0] # 처음 집에는 공유기를 무조건 설치할 수 있기 때문에 value값에 처음 집 좌표 저장
    cnt = 1 # 처음 집은 무조건 설치 했기때문에 공유기 설치 카운트 수 1로 설정

    for i in range(1, N): # 처음 집은 설치 했기 때문에 다음 집부터 마지막 집까지 반복문 실행
        if N_list[i] >= value + mid: # i번째 집 좌표값이 value + mid보다 크거나 같으면
            value = N_list[i] # 공유기를 설치할 수 있기때문에 value값에 집 좌표를 갱신
            cnt += 1 # 공유기를 설치했기 때문에 카운트값 +1

    # 공유기 설치 카운드 값이 설치해야되는 개수보다 크거나 같으면, start값을 mid + 1해서
    # 집과 집 사이의 걸이가 더 멀어도 설치해야하는 공유기 개수만큼 설치가 가능한지 확인
    if cnt >= C: 
        start = mid + 1
        result = mid # 우선 결과값에 현재 mid값 저장(mid값이 공유기 C개를 설치할 수 있는 거리)
    # 공유기를 설치할 수 있는 개수가 부족하다면, end값을 mid - 1 해서
    # 공유기를 더 설치할 수 있는지 확인
    else:
        end = mid - 1

print(result)

# 제출 결과, 틀림 -> 반례를 찾아봄
# 3 3
# 1
# 4
# 6
# 출력 : 2(내 코드에서의 출력 : 0)
# 코드 확인해보니까, start 초기 설정 부분에서 이상함을 느낌
# start값을 N_list[1] - N_list[0]으로 설정했을 떄, 반례의 start값이 3이 나옴
# 원래는 1이 나와야하며, 문제의 예제에서 1로 나오는 예제였기 때문에 아무 이상 없었던 것이었음
# start값을 1로 초기화시켜준 후, 반례를 다시 실행하였더니 출력값이 2가 나옴