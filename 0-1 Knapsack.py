#Using recursion

#wt = Weights of items
#val = Price of items
#W= Capacity of Knapsack
#n = number of items
'''
def Knapsack(wt,val,W,n):

    if n==0 or W==0:
        return 0

    if wt[n-1]>W:
        return Knapsack(wt,val,W,n-1)

    else:
        return max(val[n-1]+Knapsack(wt,val,W-wt[n-1],n-1), Knapsack(wt,val,W,n-1))


val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(Knapsack(wt,val,W,n)) 
'''

#Using 2D matrix

'''
def knapSack(W,wt,val,n):

    if n==0 or W==0:
        return 0

    table = [[0 for i in range(W+1)] for j in range(n+1)]
             
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                table[i][j]=0

            elif wt[i-1]>j:
                table[i][j] = table[i-1][j]

            else:
                table[i][j] = max(table[i-1][j],val[i-1]+table[i-1][j-wt[i-1]])


    return table[n][W]
        
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W,wt,val,n)) 

'''
