import sys

N = int(sys.stdin.readline())
WordArr = []

for i in range(N):
    WordArr.append(sys.stdin.readline().strip())

WordArr = list(set(WordArr))
WordArr.sort()
WordArr.sort(key = len)

for i in WordArr:
    print(i)

# import sys

# N = int(sys.stdin.readline())
# WordArr = []

# for i in range(N):
#     Word = sys.stdin.readline().strip()
#     if Word not in WordArr:
#         WordArr.append(Word)

# WordArr.sort()
# WordArr.sort(key = len)

# for i in WordArr:
#     print(i)