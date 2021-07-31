def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        dp[0] = 1
        
        for i in range(1,n):
            
            for j in range(i):
                if nums[j]<nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    
        return max(dp)
                    
