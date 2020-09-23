#Length of shortest common supersequence

def lcs(a,b,n,m):

    if a=="":
        return b

    if b=="":
        return a


    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])


    return dp[n][m]


a = 'AGGTAB'
b = 'GXTXAYB'

l = lcs(a,b,len(a),len(b))
print(len(a)+len(b)-l)

#lcs = 'GTAB'
'''
The worst condition can be if we take both the strings and form a single string - 'AGGTABGXTXAYB'. This string contains both the strings hence is supersequence.
But we want shortest supersequence, so we will remove the characters common in both the strings without disturbing the order. It is only possible if we remove the
longest common subsequence. After removing the length of lcs from the sum of lengths of both the strings[len(a)+len(b)-len(lcs)], we will get the length of shortest supersequence.

'''
