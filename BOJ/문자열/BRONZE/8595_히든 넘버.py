import sys

sys.stdin = open("input.txt","rt")
n = int(sys.stdin.readline())
S = sys.stdin.readline()

# 입력받은 문자열에서 소문자 제거
for i in range(26):
    S = S.replace(chr(97 + i), ' ')

# 입력받은 문자열에서 대문제 제거
for i in range(26):
    S = S.replace(chr(65 + i), ' ')

# split() 함수를 이용하여 공백을 제거한 후, 히든 숫자를 모두 더한 값 출력
print(sum(list(map(int, S.split()))))