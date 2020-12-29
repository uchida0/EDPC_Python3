from collections import defaultdict

def b_1(N:int, K:int, h_cost:list):
    for i in range(0,N):
        dp[i] = float("inf")
    dp[0] = 0
    #経路記憶用
    before_root = [0 for i in range(0,N)]

    for j in range(0,N):
        # +Kが範囲なのでrange()を使う場合に注意
        for k in range(j,j+K+1):
            if k >= N:
                break
            #経路記憶処理
            if dp[k] != min(dp[k], dp[j]+abs(h_cost[j]-h_cost[k])):
                before_root[k] = j
                dp[k] = dp[j]+abs(h_cost[j]-h_cost[k])

            #dp[k] = min(dp[k], dp[j]+abs(h_cost[j] - h_cost[k]))
    
    print("b_1: " + str(dp[N-1]))
    print(dp)
    #print(before_root)
    #以下、N-1の最適経路を導出する処理
    result_root = []
    result_root.append(N-1)
    root = before_root[N-1]
    
    while root != 0:
        result_root.append(root)
        root = before_root[root]
    
    result_root.append(0)
    result_root.reverse()
    print(result_root)



if __name__ == "__main__":
    dp = defaultdict(int)
    N, K = map(int, input().split())
    h_cost = list(map(int, input().split()))
    b_1(N, K, h_cost)