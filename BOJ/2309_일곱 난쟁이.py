import sys
import itertools

N = [int(sys.stdin.readline()) for _ in range(9)]

for i in itertools.combinations(N, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break

# import sys

# N = []

# for i in range(9):
#     N.append(int(sys.stdin.readline()))

# Sum_Dwarf_Height = sum(N)

# for i in range(9):
#     for j in range(i + 1, 9):
#         if Sum_Dwarf_Height - (N[i] + N[j]) == 100:
#             Fake_Dwarf1 = N[i]
#             Fake_Dwarf2 = N[j]
#             N.remove(Fake_Dwarf1)
#             N.remove(Fake_Dwarf2)
#             N.sort()
#             for i in N:
#                 print(i)
#             sys.exit(0)