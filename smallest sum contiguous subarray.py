import sys

minsofar = sys.maxsize
minending = 0
dp = [0]*len(a)
n=len(a)

for i in range(len(a)):
    
    minending += a[i]
    if minending<dp[i]:
        dp[i] = minending
        
    else:
        minending = 0

print(min(dp))

                    
