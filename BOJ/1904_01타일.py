import sys

def DP(n):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 1000001
    # 1, 2번째 피보나치 수 1, 2으로 초기화
    d[1], d[2] = 1, 2

    # n개의 타일로 만들 수 있는 2진 수열의 개수 계산
    for i in range(3, n + 1):
        d[i] = (d[i - 2] + d[i - 1]) % 15746

    return d[n]

if __name__ == "__main__":
    # 정수 n 입력
    n = int(sys.stdin.readline())
    
    # n개의 타일로 만들 수 있는 2진 수열의 개수 출력
    print(DP(n))