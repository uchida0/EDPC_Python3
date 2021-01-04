"""
N頂点M辺の有向グラフG
Gは有向閉路を含まない
Gの有向パスのうち最長の長さを求める。

トポロジカルソート
step1: 入次数と出次数を頂点毎に整理
step2: 入次数が0の頂点からqueに入れていき、その頂点についての情報を消す
step3: step2を繰り返して残る頂点がないときに終了となり、
　　　 トポロジカルオーダーが得られる
"""
from collections import deque


def g():
    N, M = map(int, input().split())
    adjL = [[] for v in range(N)]
    indegs = [0] * N

    #indexがずれる
    for _ in range(M):
        x, y = map(int, input().split())
        adjL[x-1].append(y-1)
        indegs[y-1] += 1
    
    dp = [0] * N
    Q = deque([v for v in range(N) if indegs[v] == 0])
    #print(Q)

    while Q:
        v_now = Q.popleft()
        for v2 in adjL[v_now]:
            dp[v2] = max(dp[v2], dp[v_now] + 1)
            indegs[v2] -= 1
            if indegs[v2] == 0:
                Q.append(v2)
                #print(Q)
    
    #print()
    print(max(dp))


if __name__ == "__main__":
    g()