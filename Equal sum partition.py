def subsetSum(arr,W,n):

    t = [[False for i in range(W+1)] for j in range(n+1)]

    for i in range(n+1):
        t[i][0]=True

    for j in range(1,W+1):
        t[0][j]=False

    for i in range(1,n+1):
        for j in range(1,W+1):

            if arr[i-1]>j:
                t[i][j]=t[i-1][j]

            else:
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]

    return t[n][W]


def partitionSet(arr):

    if sum(arr)%2!=0:
        print("False")
    else:
        print(subsetSum(arr,sum(arr)//2,len(arr)))

a=[5,5,3,3,1,1]
partitionSet(a)


