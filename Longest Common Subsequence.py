
def longestSubsequence(X,Y,n,m):

    t = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):

            if t[i][j]!=-1:
                return t[i][j]

            if X[i-1]==Y[j-1]:
                t[i][j] = 1+t[i-1][j-1]

            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])


    return t[n][m]


s = "abxc"
t = "abdfxyc"
print(longestSubsequence(s,t,4,7))
                














