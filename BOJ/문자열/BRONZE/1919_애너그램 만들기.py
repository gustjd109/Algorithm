# 입력받은 첫 번째 문자열의 영어 단어를 아스키 코드로 변환하고 97을 뺀 값에 해당하는 알파벳 리스트의 인덱스 값 1 증가시킨다.
# 입력받은 두 번째 문자열의 영어 단어를 아스키 코드로 변환하고 97을 뺀 값에 해당하는 알파벳 리스트의 인덱스 값 1 감소시킨다.
# 이렇게 하면, 알파벳 리스트에는 두 문자열의 중복되는 영어 단어는 빼지고, 서로 다른 영어 단어 개수만 남게 된다.
# 마지막으로, 알파벳 리스트의 각 인덱스의 값에 절대값을 추가하여 결과값에 더해준다.

import sys

sys.stdin = open("input.txt","rt")
S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
alphabet = [0] * 26
remove_alphabet_cnt = 0

for i in range(len(S1)):
    alphabet[ord(S1[i]) - 97] += 1

for i in range(len(S2)):
    alphabet[ord(S2[i]) - 97] -= 1

for i in alphabet:
    remove_alphabet_cnt += abs(i)

print(remove_alphabet_cnt)