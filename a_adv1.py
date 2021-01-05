"""
https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

1 <= N <= 100, 1<= pi <=100
N問の問題があるコンテスト
i問目の配点はpi点
コンテストの得点は何通りあるか？

Input Format
N
p1 p2 p3 p4

取りうる得点がTrueであるかどうか
"""

def a_adv1():
    N = int(input())
    P = list(map(int, input().split()))

    dp = [False for _ in range(N*100+1)]
    dp[0] = True

    for p in P:
        new_dp = dp[:]
        for i in range(N*100+1):
            if p+i < N*100+1 and dp[i]:
                new_dp[p+i] = True
        
        dp = new_dp[:]
    
    result = 0

    for d in dp:
        if d:
            result += 1
    
    print(result)





if __name__ == "__main__":
    a_adv1()
