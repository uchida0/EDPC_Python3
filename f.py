"""
1<= |s|,|t| <= 3000
LCSから復元
"""

def e():
    s: str = input()
    t: str = input()

    s_length, t_length = len(s), len(t)
    
    dp = [[0]*(t_length+1) for _ in range(s_length+1)]

    for i in range(s_length):
        for j in range(t_length):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            #print(dp)
    
    #print(dp[-1][-1])

    result = ""

    while s_length>0 and t_length>0:
        if dp[s_length][t_length] == dp[s_length-1][t_length]:
            s_length -=1
        elif dp[s_length][t_length] == dp[s_length][t_length-1]:
            t_length -=1
        else:
            s_length -=1
            t_length -=1
            result += s[s_length]
    
    print(result[::-1])



if __name__ == "__main__":
    e()