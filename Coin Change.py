#Number of ways for exchanging coins

#arr = values of coin
#W = change to make
#n = length of array

def changeCoin(arr,W,n):

    t = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):

            if arr[i-1]>j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = t[i-1][j] + t[i][j-arr[i-1]]

    return t[n][W]
 
arr=[2,5,3,6]
s=10
print(changeCoin(arr,s,4))






