# 조합(combinations) 라이브러리를 이용한 풀이
import sys
import itertools

sys.stdin = open("input.txt","rt")
N = [int(sys.stdin.readline()) for _ in range(9)]

for i in itertools.combinations(N, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break

# 브루트포스 알고리즘을 이용한 풀이
import sys

sys.stdin = open("input.txt","rt")
Dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
Sum_Dwarfs_Height = sum(Dwarfs)

for i in range(8):
    for j in range(i + 1, 9):
        if Sum_Dwarfs_Height - Dwarfs[i] - Dwarfs[j] == 100:
            Fake_Dwarf1 = Dwarfs[i]
            Fake_Dwarf2 = Dwarfs[j]
            Dwarfs.remove(Fake_Dwarf1)
            Dwarfs.remove(Fake_Dwarf2)
            Dwarfs.sort()
            print(*Dwarfs, sep='\n')
            sys.exit(0)