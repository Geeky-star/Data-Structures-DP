
def lcs(a,b,n,m):

    if a=="":
        return len(b)

    if b=="":
        return len(a)

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if a[i-1]==b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[n][m]


a = 'heap'
b='pea'

l = lcs(a,b,len(a),len(b))
res = len(a)-l
ans = len(b)-l
print(res+ans)
