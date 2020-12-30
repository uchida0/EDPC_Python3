"""
Wの制約が変化
1 <= N <= 100
D: 1 <= W <= 10**5　　1 <= vi <= 10**9
E: 1 <= W <= 10**9    1 <= vi <= 10**3
重さを軸にするとテーブルサイズがO(NW)で、膨大になるので・・・
"""
"""
DPテーブルとweight,valueのインデックスがずれている
"""

def e():
    N, W = map(int, input().split())
    weight = [0 for _ in range(0,N)]
    value = [0 for _ in range(0,N)]
    for i in range(0,N):
        weight[i], value[i] = map(int, input().split())
    
    #print(weight)
   # print(value)

    MAX_V = sum(value)

    dp = [[float("inf")]*MAX_V for _ in range(0,N+1)]
    dp[0][0] = 0

    for i in range(0,N):
        for sum_v in range(0,MAX_V):
            if (sum_v - value[i]) >= 0:
                dp[i+1][sum_v] = min(dp[i][sum_v], dp[i][sum_v-value[i]] + weight[i])
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])
    
    result = 0

    #探索部が正常に動いてないかも
    for sum_v in range(0, MAX_V):
        if dp[N][sum_v] <= W:
            result = max(sum_v,result)
    
    print(result)





if __name__ == "__main__":
    e()