class Solution:
    def largest(self, arr):
        
        maximum = arr[0]   
        
        for num in arr:
            if num > maximum:
                maximum = num
                
        return maximum

        
