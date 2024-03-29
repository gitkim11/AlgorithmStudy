import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N - 1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(max(dp))
