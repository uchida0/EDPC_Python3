def c():
    N = int(input())

    action = [[0]*3 for _ in range(N)]
    for n in range(0,N):
        action_list = list(map(int, input().split()))
        for a in range(0,3):
            action[n][a] = action_list[a]

    dp = [[0]*3 for _ in range(N)]

    for a in range(0,3):
        dp[0][a] = action[0][a]


    for i in range(1,N):
        for j in range(0,3):
            for k in range(0,3):
                if j == k:
                    continue
                dp[i][k] = max(dp[i][k], dp[i-1][j]+action[i][k])
    

    result = 0

    for a in range(0,3):
        result = max(result, dp[N-1][a])
    
    print(result)




if __name__ == "__main__":
    #N = int(input())
    c()