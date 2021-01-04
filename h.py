"""
H,W: int
a[][] => "." or "#"
グリッドの経路数
10**9+7　でmod
2 <= H,W <= 1000

経路の合流地点について考えていけばよい
"""

from collections import defaultdict

MOD = 10**9 + 7

def h():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    #print(G)

    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if G[i][j] == "#":
                continue
            dp[i][j] %= MOD
            if i < H-1:
                dp[i+1][j] += dp[i][j]
            if j < W-1:
                dp[i][j+1] += dp[i][j]

    print(dp[-1][-1])
    


if __name__ == "__main__":
    h()