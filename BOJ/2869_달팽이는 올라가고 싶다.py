import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
print(math.ceil((V - A) / (A -B)) + 1)

# 달팽이는 올라갔다가 미끄러지기를 N번 반복하고, 마지막날은 올라가기만 함
# 마지막 날은 올라가다가 이미 정상에 도달하여 미끄러지지 않음
# 위 내용을 식으로 만들어보면 -> V = (A - B) * N + A -> N = (V - A) / (A - B)으로 나타낼 수 있음
# 위 식을 이용했을 때의 문제점은 나머지가 생긴다는 것임
# 따라서 파이썬 math 모듈의 ceil(올림 함수)를 이용하여 올려주고, 하루를 더해줘야 함
# 최종 식은 -> math.ceil((V - A) / (A - B)) + 1되어야 함