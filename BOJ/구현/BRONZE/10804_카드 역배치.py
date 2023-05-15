# 단순 탐색을 이용한 풀이
import sys

sys.stdin = open("input.txt","rt")
cards = [i + 1 for i in range(20)]
for _ in range(10):
    A, B = map(int, sys.stdin.readline().split())
    print(A, B)
    reverse_cards = []
    for i in range(A, B + 1):
        reverse_cards.append(cards[i - 1])
    reverse_cards = reverse_cards[::-1] # reverse_cards.sort(reverse=True)
    print(reverse_cards)
    for j in range(A, B + 1):
        cards[j - 1] = reverse_cards[j - A]
print(*cards)

# 문자열 슬라이스 기능을 이용한 풀이
import sys

sys.stdin = open("input.txt","rt")
cards = [i + 1 for i in range(20)]

for i in range(10):
    A, B = map(int, sys.stdin.readline().split())
    back_cards=cards[:A - 1]
    mid_cards = cards[A - 1:B][::-1]
    front_cards=cards[B:]
    cards=back_cards + mid_cards + front_cards
print(*cards)

# 수 두개씩 바꾸는 것을 이용한 풀이
import sys

sys.stdin = open("input.txt","rt")
cards = [i + 1 for i in range(20)]

for _ in range(10):
    A, B = map(int, sys.stdin.readline().split())
    for i in range(A, B - ((B - A) // 2)):
        cards[i - 1], cards[B - i + A - 1] = cards[B - i + A - 1], cards[i - 1]
print(*cards)