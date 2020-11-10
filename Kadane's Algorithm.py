import sys

def maxSubArraySum(a,size):
    
    max_so_far = -sys.maxsize
    max_ending_here = 0
    
    for i in range(size):
        max_ending_here += a[i]
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
        if max_ending_here<0:
            max_ending_here = 0
            
    return max_so_far
