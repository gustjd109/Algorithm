# 학생을 학년과 성별을 구분하여 배열에 저장한다.
# 배열을 탐색하면서 같은 학년의 성별이 다른 학생 수를 K로 나눈 몫만큼 방 카운트 값을 증가시켜 준다.
# 만약, 학생 수를 K로 나눴을 때 나머지가 있으면 방 카운트 변수에 1 증가시켜 준다.
import sys

sys.stdin = open("input.txt","rt")
N, K = map(int, sys.stdin.readline().split())
students = [[0, 0] for _ in range(6)]
room_cnt = 0

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    students[Y - 1][S] += 1

for grade in students:
    for sex in grade:
        room_cnt += sex // K
        if sex % K:
            room_cnt += 1

print(room_cnt)