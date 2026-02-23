from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
       
        target_pos = (n * m // 2) + 1
        
       
        low = mat[0][0]
        high = mat[0][m-1]
        for i in range(1, n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][m-1])
            
        ans = low
        while low <= high:
            mid = (low + high) // 2
            count = 0
          
            for i in range(n):
                count += bisect_right(mat[i], mid)
            
            if count < target_pos:
               
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
                
        return ans
