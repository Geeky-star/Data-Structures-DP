def longestUnivaluePath(self, root: TreeNode) -> int:        
        def solve(root):
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                return 1
            
            l = solve(root.left)
            r = solve(root.right)
            
            if l!=0 and root.val!=root.left.val:
                l=0
                
            if r!=0 and root.val!=root.right.val:
                r=0
                
            temp=max(l,r)+1
            ans=max(temp,l+r+1)
            solve.res=max(solve.res,ans)
            
            return temp
        
        solve.res=0
        solve(root)
        return max(0,solve.res-1)
    
    
            
