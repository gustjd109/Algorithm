import sys

def greedy():
    # 처음 회의는 회의실을 사용한 것으로 간주하고 회의실을 사용한 회의 개수 1로 초기화
    cnt = 1
    # 회의 종료 시간을 처음 회의실을 사용한 회의의 종료 시간으로 설정
    end = meetings[0][1]
    # 처음 회의는 회의실을 사용했으므로 다음 회의부터 탐색 시작
    for i in range(1, N):
        # 만약, i번째 회의의 시작 시간이 마지막으로 회의실을 사용한 회의의 종료 시간보다 같거나 크면
        if meetings[i][0] >= end:
            # 회의실을 사용한 회의 개수 1증가
            cnt += 1
            # 회의 종료 시간을 i번째 회의의 종료 시간으로 갱신
            end = meetings[i][1]
    print(cnt)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 회의 개수 입력
    N = int(sys.stdin.readline())
    # 회의의 시작 시간과 끝나는 시간 입력
    meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 종료 시간을 기준으로 오름차순 정렬
    # 다음으로 그 안에서 시작 시간을 기준으로 오름차순 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    greedy()