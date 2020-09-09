#wt - weight area
#val - values of given weights
#W - Knapsack capacity
#n - length of weight array

def unboundKnapsack(wt,val,W,n):

    t = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]>j:
                t[i][j]=t[i-1][j]

            else:
                t[i][j] = max(t[i-1][j], val[i-1]+t[i][j-wt[i-1]])

    return t[n][W]

W = 100
val= [1, 30]
wt = [1, 50]
print(unboundKnapsack(wt,val,W,2))






