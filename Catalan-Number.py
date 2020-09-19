#nth Catalan number
'''
Applications-
 1. Used to find number of binary search trees with given n keys
 2. Count number of full binary trees with n+1 leaves
 3. Count number of valid expressions that can be formed using n pairs of parenthesis
 4. Given number n, return number of ways to draw a chord in a circle with 2*n points such that no 2 chords intersect
'''
#Recursive method

def catalan(n):
    res=0
    if n<=1:
        return 1

    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)

    return res


print(catalan(4))


#DP approach

def catalan(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=0
        for j in range(i):
            dp[i]= dp[i] + dp[j]*dp[i-j-1]

    return dp[n]

print(catalan(9))



