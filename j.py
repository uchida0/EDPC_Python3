"""
1 <= N <= 300
1 <= ai <= 3
N個の出目が等確率

各皿の状態を管理すると状態量が爆発する
=> 寿司の状態4パターン
=> 4**N

寿司の個数を基に状態を管理する
dp[i][j][k]
i:寿司1個
j:寿司2個
k:寿司3個
dp[i][j][k]=(
            dp[i-1][j][k]*i/N 
            +dp[i+1][j-1][k]*j/N
            +dp[i][j+1][k-1]*k/N
            +1
            )*N/(i+j+k)

"""

from collections import Counter

def j():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = Counter(A)

    dp = [[[0.0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

    #print(dp)

    process_all = 0

    for k in range(N+1):
        for j in range(N+1-k):
            for i in range(N+1-k-j):
                if i > 0:
                    #dp[i][j][k] += dp[i-1][j][k]*i/N
                    process_all += dp[i-1][j][k]*i/N
                if j > 0:
                    #dp[i][j][k] += dp[i+1][j-1][k]*j/N
                    process_all += dp[i+1][j-1][k]*j/N
                if k > 0:
                    #dp[i][j][k] += +dp[i][j+1][k-1]*k/N
                    process_all += dp[i][j+1][k-1]*k/N
                if i+j+k > 0:
                    #dp[i][j][k] = (dp[i][j][k]+1)*N/(i+j+k)
                    dp[i][j][k] += (process_all + 1)*N/(i+j+k)
                    process_all = 0
    
    result = dp[cnt[1]][cnt[2]][cnt[3]]

    print(result)
                




if __name__ == "__main__":
    j()
