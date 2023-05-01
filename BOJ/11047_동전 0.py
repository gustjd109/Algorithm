import sys

def greedy(K):
    # K원을 만드는데 필요한 동전 개수 0으로 초기화
    result = 0
    # 모든 동전을 순차적으로 탐색
    for coin in coins:
        # 만약 금액이 0원 이하이면 반복문 탈출
        if K <= 0:
            break
        # 남은 금액이 동전보다 같거나 크면 금액을 동전으로 나눈 몫을 결과 변수에 추가한 후, 나머지를 금액에 재할당
        if K >= coin:
            result += K // coin
            K %= coin
    # 결과값 출력
    print(result)

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 동전 종류 N, 금액 K 입력
    N, K = map(int, sys.stdin.readline().split())
    # N개의 동전 종류 입력
    coins = [int(sys.stdin.readline()) for _ in range(N)]
    # 큰 금액의 동전부터 나누기 위해 동전 종류 내림차순 정렬
    coins.sort(reverse=True)
    # 그리디 알고리즘 수행
    greedy(K)