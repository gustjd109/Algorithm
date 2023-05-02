import sys

def greedy():
    # 제일 처음 지원자는 서류 순위가 1등이므로 무조건 채용하기 때문에 결과값 1로 초기화
    result = 1
    # 현재 지원자의 면접 순위를 비교할 지원자 면접 순위
    min = applicant_list[0][1]
    # 지원자 수만큼 반복문 수행
    for i in range(1, N):
        # 현재 지원자의 면접 순위가 이전 지원자의 면접 순위보다 높으면 채용이므로 결과값 1증차
        if applicant_list[i][1] < min:
            result += 1
            # 현재 지원자의 면접 순위를 비교할 지원자 면접 순위 갱신(더 이전 지원자의 면접 순위와는 비교할 필요가 없음)
            min = applicant_list[i][1]
    # 결과값 출력
    print(result)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 테스트 케이스 입력
    T = int(sys.stdin.readline())
    # 테스트 케이스만큼 반복문 수행
    for _ in range(T):
        # 지원자 수 입력
        N = int(sys.stdin.readline())
        # 지원자 서류, 면접 순위 입력
        applicant_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        # 지원자 서류 순위를 기준으로 오름차순 정렬
        applicant_list.sort(key=lambda x: x[0])
        # 그리디 알고리즘 수행
        greedy()