# Using Recursion

import sys

def MatrixChainOrder(p,i,j):

    if i==j:
        return 0

    _min = sys.maxsize

    for k in range(i,j):

        count = MatrixChainOrder(p,i,k) +MatrixChainOrder(p,k+1,j) + p[i-1]*p[k]*p[j]

        if count<_min:
            _min = count


    return _min


#Using Dynamic Programming


import sys

def MatrixChainOrder(p,n):

    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(1,n):
        dp[i][i]=0

    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            dp[i][j] = sys.maxsize
            for k in range(i,j):
                q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]

                if q<dp[i][j]:
                    dp[i][j]=q

    return dp[1][n-1]
