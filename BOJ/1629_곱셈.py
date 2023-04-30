# 분할 정복과 재귀함수를 이용한 풀이
import sys

def divide(A, B, C):
    # B가 1이면 A % C를 리턴
    if B == 1:
        return A % C
    # B가 짝수이면, tmp에 A^B//2 * A^B//2 % C값 저장(이때, A % C가 될때까지 divide함수 재귀호출)
    elif B % 2 == 0:
        tmp = divide(A, B // 2, C)
        return tmp * tmp % C
    # # B가 홀수이면, tmp에 A * A^B//2 * A^B//2 % C값 저장(이때, A % C가 될때까지 divide함수 재귀호출)
    else:
        tmp = divide(A, B // 2, C)
        return A * tmp * tmp % C

if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    print(divide(A, B, C))

# 파이썬 제곱 함수 pow를 이용한 풀이
import sys
A, B, C = map(int, sys.stdin.readline().split())
print(pow(A, B, C))