def lcs(x,y,z,n,m,k):

    dp=[[[0 for i in range(k+1)] for j in range(m+1)] for s in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            for a in range(k+1):
                if i==0 or j==0 or a==0:
                     dp[i][j][a] = 0

                elif x[i-1]==y[j-1]==z[a-1]:
                     dp[i][j][a]=1+dp[i-1][j-1][a-1]

                else:
                     dp[i][j][a] = max(dp[i-1][j][a],dp[i][j-1][a],dp[i][j][a])

    return dp[n][m][k]


t=int(input())
for i in range(t):
    n,m,k = list(map(int,input().split()))
    x,y,z = input().split()
    ans = lcs(x,y,z,n,m,k)
    print(ans)


