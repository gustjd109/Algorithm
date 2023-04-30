import sys

N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
start, end = 0, N - 1
# 두 용액을 합한 특성값이 0에 가까운 두 용액을 저장하는 리스트
result = []
# 두 용액을 합한 특성값을 비교하여 더 작은 값을 저장 하기 위한 변수
min_val = sys.maxsize

# N개의 용액들의 특성값은 모두 다르다는 조건에 의해 <=가 아닌 <로 해줘야 함
while start < end:
    # 두 용액의 특성값을 더한 값을 저장하기 위한 임시 변수
    tmp = N_list[start] + N_list[end]
    # 두 용액의 특성값을 더한 절대값이 min_val보다 작다면
    # 절대값으로 변환하여 저장하는 이유 : 0까지의 차이값을 구하는 것이기에 음수이든 양수이든 상관 없기 때문이다.
    if abs(tmp) < min_val:
        # min_val에 두 용액의 특성값을 더한 절대값을 저장
        min_val = abs(tmp)
        # 결과값에 두 용액의 특성값 저장
        result = (N_list[start], N_list[end])
    # 두 용액의 특성값을 더한 값이 0보다 작다면, start값에 +1
    # 0에 가까운 값으로 만들기 위해 더 작은 음수값을 더하기 위함
    if tmp < 0:
        start += 1
    # 두 용액의 특성값을 더한 값이 0보다 크다면, end값에 -1
    # 0에 가까운 값으로 만들기 위해 더 작은 양수값을 더하기 위함
    elif tmp > 0:
        end -= 1
    # 두 용액의 특성값을 더한 값이 0이거나, 투 포인터 검색이 끝나면 프로그램 종료
    else:
        break
# 검색이 끝난 후, 저장된 두 용액의 특성값 출력
print(*result)