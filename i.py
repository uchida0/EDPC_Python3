"""
Nは奇数
1 <= N <= 2999
piは実数、小数第2位まで与えられる
0< pi <1

コインi => 表: pi 裏：1-pi

表の個数が裏の個数を上回る確率を求める

i枚のコインを投げたとき、表がj枚の確率
状態遷移を記述していくだけ
"""

def i():
    N = int(input())
    P = list(map(float,input().split()))

    #P_back = [1-p_f for p_f in P_front]

    dp = [[0.0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1.0

    for i in range(N):
        for j in range(i+1):
            dp[i+1][j+1] += dp[i][j] * P[i]
            dp[i+1][j] += dp[i][j] * (1-P[i])
    
    result = 0.0

    for j in range((N+1)//2, N+1):
        result += dp[N][j]
    
    print(result)




if __name__ == "__main__":
    i()