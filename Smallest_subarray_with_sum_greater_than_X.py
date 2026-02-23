class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        current_sum = 0
        min_len = n + 1
        left = 0
        
        for right in range(n):
           
            current_sum += arr[right]
            
           
            while current_sum > x:
                
                min_len = min(min_len, right - left + 1)
                
               
                current_sum -= arr[left]
                left += 1
                
       
        return min_len if min_len <= n else 0
