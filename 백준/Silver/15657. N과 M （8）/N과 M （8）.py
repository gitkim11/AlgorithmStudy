import sys

input = sys.stdin.readline

N, M = map(int, input().split())
elements = list(map(int, input().split()))
elements.sort()
s = []

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(start, len(elements)):
        s.append(elements[i])
        dfs(i)
        s.pop()
dfs(0)
