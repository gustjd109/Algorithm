import sys

def AppendColRowData(nCutNum):
    for i in range(0, nCutNum):
        nColRowFlag, ColRowData = map(int, sys.stdin.readline().split())
        if nColRowFlag == 0:
            lRows.append(ColRowData)
        else:
            lCols.append(ColRowData)

def CalArea(lCols, lRows):
    nMaxArea = 0
    for i in range(len(lRows) - 1):
        for j in range(len(lCols) - 1):
            nMaxArea = max(nMaxArea, ((lCols[j + 1] - lCols[j]) * (lRows[i + 1] - lRows[i])))
    print(nMaxArea)

nCol, nRow = map(int, sys.stdin.readline().split())
nCutNum = int(sys.stdin.readline())
lCols = [0, nCol]
lRows = [0, nRow]

AppendColRowData(nCutNum)
lRows.sort()
lCols.sort()
CalArea(lCols, lRows)

# import sys

# def AppendColRowData(nCutNum):
#     for _ in range(nCutNum):
#         nColRowFlag, ColRowData = map(int, sys.stdin.readline().split())
#         if nColRowFlag == 0:
#             lRows.append(ColRowData)
#         else:
#             lCols.append(ColRowData)

# def SortRowsData(lRows):
#     for i in range(len(lRows) - 1):
#         for j in range(i + 1, len(lRows)):
#             Tmp = 0
#             if lRows[i] > lRows[j]:
#                 Tmp = lRows[i]
#                 lRows[i] = lRows[j]
#                 lRows[j] = Tmp

# def SortColsData(lCols):
#     for i in range(len(lCols) - 1):
#         for j in range(i + 1, len(lCols)):
#             Tmp = 0
#             if lCols[i] > lCols[j]:
#                 Tmp = lCols[i]
#                 lCols[i] = lCols[j]
#                 lCols[j] = Tmp

# def CalArea(lCols, lRows):
#     nMaxArea = 0
#     for i in range(len(lRows) - 1):
#         for j in range(len(lCols) - 1):
#             nArea = (lCols[j + 1] - lCols[j]) * (lRows[i + 1] - lRows[i])
#             if nArea > nMaxArea:
#                 nMaxArea = nArea
#     print(nMaxArea)

# nCol, nRow = map(int, sys.stdin.readline().split())
# nCutNum = int(sys.stdin.readline())
# lCols = [0, nCol]
# lRows = [0, nRow]

# AppendColRowData(nCutNum)
# SortColsData(lRows)
# SortRowsData(lCols)
# CalArea(lCols, lRows)