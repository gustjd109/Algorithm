import sys
from collections import deque

def topology():
    # 학생의 키 순서를 저장할 빈 리스트
    result = []
    # 큐 구현을 위해 deque 라이브러리 사용
    q = deque()

    # 진입 차수가 0인 학생을 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 비어있지 않으면 반복분 수행
    while q:
        # 큐에서 학생의 정보를 삭제
        now = q.popleft()
        # 결과값 저장 리스트에 꺼낸 학생 번호 삽입
        result.append(now)

        # 꺼낸 학생으로부터 진입 차수가 존재하는 학생들의 진입 차수 - 감소
        for i in graph[now]:
            indegree[i] -= 1
            # 진입 차수가 0인 학생이라면 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 키 순서대로 정렬된 학생의 번호 출력
    for i in result:
        print(i, end=' ')
    print()

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 학생 수 N, 키 비교 횟수 M 입력
    N, M = map(int, sys.stdin.readline().split())
    # 진입차수 0으로 초기화
    indegree = [0] * (N + 1)
    # 두 학생의 번호 정보를 삽입할 빈 연결리스트 초기화
    graph = [[] for _ in range(N + 1)]

    # 두 학생의 번호 정보 삽입
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        # 삽입한 학생의 진입차수 1 증가
        indegree[b] += 1

    # 위상 정렬 알고리즘 수행
    topology()