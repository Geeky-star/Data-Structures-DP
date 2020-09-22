def minSum(a,n):

    minsofar = 100001
    minend = 100001

    for i in range(n):

        if minend>0:
            minend = a[i]

        else:
            minend += a[i]
            
        minsofar = min(minend,minsofar)

    return minsofar

a = [3,-4,2,-3,-1,7,-5]
print(minSum(a,len(a)))




