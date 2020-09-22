
#Largest cotiguous subset sum

#Kadane's Algorithm

def maxSum(a,n):

    maxsofar = -100001
    maxend = 0

    for i in range(n):
        maxend+=a[i]
        if maxend>maxsofar:
            maxsofar = maxend

        if maxend<0:
            maxend=0

    return maxsofar


a = [-2,-3,4,-1,-2,1,5,-3]
print(maxSum(a,len(a)))
