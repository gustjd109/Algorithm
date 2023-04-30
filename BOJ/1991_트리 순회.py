import sys

def preorder(P):
    if P != '.':
        print(P, end='')
        preorder(graph[P][0])
        preorder(graph[P][1])

def inorder(P):
    if P != '.':
        inorder(graph[P][0])
        print(P, end='')
        inorder(graph[P][1])

def postorder(P):
    if P != '.':
        postorder(graph[P][0])
        postorder(graph[P][1])
        print(P, end='')

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    graph = {}
    for _ in range(N):
        P, LC, RC = sys.stdin.readline().strip().split()
        graph[P] = [LC, RC]
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    print()