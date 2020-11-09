def maxChainLen(Parr, n):
    l=[]
    for i in range(n):
        l.append([Parr[i].a,Parr[i].b])
        
    l=sorted(l)
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if l[i][0]>l[j][1] and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
            
    return max(dp)
