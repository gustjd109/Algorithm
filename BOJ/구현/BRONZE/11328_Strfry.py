# 입력받은 두 개의 문자열을 정렬한다.
# 정렬된 두 개의 문자열을 비교하여 같으면 Possible, 다르면 Impossible을 출력한다.

import sys

sys.stdin = open("input.txt","rt")
T = int(sys.stdin.readline())

for _ in range(T):
    S1, S2 = sys.stdin.readline().split()
    lS1 = sorted(S1)
    lS2 = sorted(S2)
    print('Possible' if lS1 == lS2 else 'Impossible')