class Solution:
	def minJumps(self, arr):
	    
        n = len(arr)
        
        if n <= 1:
            return 0
        
        if arr[0] == 0:
            return -1
        
        jumps = 1
        current_end = arr[0]
        farthest = arr[0]
        
        for i in range(1, n):
            
            if i == n - 1:
                return jumps
            
            farthest = max(farthest, i + arr[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end <= i:
                    return -1
        
        return -1
	    
