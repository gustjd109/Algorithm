X, Y, W, H = map(int, input().split())
print(min(X, Y, H - Y, W - X))

#X좌표에서 0까지의 거리 / Y좌표에서 0까지의 겨리 / X좌표에서 W좌표까지의 거리 / Y좌표에서 H좌표까지의 거리 -> 4가지 거리 중에서 제일 작은 거리가 최단거리 