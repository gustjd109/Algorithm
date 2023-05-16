# 단순 탐색을 이용한 풀이
# 카드 리스트에서 구간에 해당하는 수를 배열 하나를 생성하여 저장한 다음 역순으로 바꾸고 다시 카드에 저장시키는 풀이다.
# 저장한 수를 역순으로 바꾸는 과정에서 조금 시간이 걸렸다.
# 처음에는 단순하게 수를 역으로 정렬한다는 생각으로 reverse_cards.sort(reverse=True)를 했었다.
# 역으로 정렬된 수를 출력해 보니 잘못 출력되는 것을 확인했다.
# 저장된 수만 역으로 바꿔야 하는데, sort() 함수를 사용하니 정렬을 시켜버려서 문제가 되었던 것이었다.
# 다시 코드를 수정하고 제출했더니 성공!
import sys

sys.stdin = open("input.txt","rt")
cards = [i + 1 for i in range(20)]
for _ in range(10):
    A, B = map(int, sys.stdin.readline().split())
    print(A, B)
    reverse_cards = []
    for i in range(A, B + 1):
        reverse_cards.append(cards[i - 1])
    reverse_cards = reverse_cards[::-1] # 문제되었던 곳
    print(reverse_cards)
    for j in range(A, B + 1):
        cards[j - 1] = reverse_cards[j - A]
print(*cards)

# 문자열 슬라이스 기능을 이용한 풀이
# 해당 풀이는 문자열 슬라이스 기능을 이용한 풀이다.
# 앞/중간/뒤 구간으로 카드 리스트를 나누고, 중간 카드 리스트를 배열의 순서를 역으로 바꿔주는 [::-1]을 이용했다.
# 중간 카드 리스트를 역으로 바꾸고, 다시 앞/중간/뒤 구간을 합쳐서 새로운 카드 리스트를 만들어서 주면 된다.
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
# 예를 들어, 구간이 [5, 10]이라고 가정하자.
# 5<->10, 6<->9, 7<->8의 숫자를 교환하는 방식으로 문제를 풀면 된다.
import sys

sys.stdin = open("input.txt","rt")
cards = [i + 1 for i in range(20)]

for _ in range(10):
    A, B = map(int, sys.stdin.readline().split())
    for i in range(A, B - ((B - A) // 2)):
        cards[i - 1], cards[B - i + A - 1] = cards[B - i + A - 1], cards[i - 1]
print(*cards)