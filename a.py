"""
https://qiita.com/drken/items/dc53c683d6de8aeacf5a
"""
"""
ポイント：初期化と初期条件をしっかり行う。
"""

from collections import defaultdict

#貰うDP
def a_1(N: int, h_cost:list):
    for i in range(0,N):
        dp[i] = float("inf")
    dp[0]=0
    for j in range(0, N):
        for k in range(0,3):
            if k > j:
                break
            dp[j] = min(dp[j], dp[j-k]+abs(h_cost[j]-h_cost[j-k]))
    
    print("a_1: "+ str(dp[N-1]))
    print(dp)

#配るDP
def a_2(N: int, h_cost:list):
    for i in range(1,N):
        dp[i] = float("inf")
    dp[0] = 0
    for j in range(0,N):
        for k in range(0,3):
            if j+k >= N:
                break
            dp[j+k] = min(dp[j+k], dp[j]+abs(h_cost[j]-h_cost[j+k]))
    
    print("a_2: "+ str(dp[N-1]))
    print(dp)



if __name__ == "__main__":
    dp = defaultdict(int)
    N = int(input())
    h_cost = list(map(int, input().split()))
    a_1(N, h_cost)
    a_2(N, h_cost)



