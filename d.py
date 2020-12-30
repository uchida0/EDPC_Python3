def d():
    N, W = map(int, input().split())
    weight = [0 for _ in range(0,N)]
    value = [0 for _ in range(0,N)]
    for i in range(0,N):
        weight[i], value[i] = map(int, input().split())
    
    dp = [[0]*(W+1) for _ in range(0,N+1)]
    #print(dp)

    for i in range(0,N):
        for sum_w in range(0, W+1):
            if (sum_w - weight[i]) >= 0:
                dp[i+1][sum_w] = max(dp[i][sum_w], dp[i][sum_w - weight[i]] + value[i])
            dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])
    
    print(dp[-1][-1])



if __name__ == "__main__":
    d()