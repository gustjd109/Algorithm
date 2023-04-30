import sys

def DP(M):
    # 0 ~ 만들어야 할 금액까지의 경우의 수를 저장할 DP테이블 초기화
    d = [0] * (M + 1)
    # 각 동전별로 0개를 이용하여 0원을 만들 수 있기 때문에 DP 테이블 0번째를 1로 초기화
    d[0] = 1
    # 각 코인만큼 반복
    for coin in coins:
        # 각 코인 금액부터 반복
        for i in range(coin, M + 1):
            # 각 코인 금액부터 만들어야 할 금액까지 경우의 수를 누적하여 계산
            d[i] += d[i - coin]
    # DP테이블의 마지막 인덱스 값 반환
    return d[-1]

if __name__ == "__main__":
    sys.stdin = open("input.txt","rt")
    # 테스트 케이스 입력
    T = int(sys.stdin.readline())
    # 테스트 케이수 수만큼 반복
    for _ in range(T):
        # 동전 개수 입력
        N = int(sys.stdin.readline())
        # N가지 동전의 각 금액 입력
        coins = list(map(int, sys.stdin.readline().split()))
        # N가지 동전으로 만들어야 할 금액 입력
        M = int(sys.stdin.readline())
        #  결과값 출력
        print(DP(M))