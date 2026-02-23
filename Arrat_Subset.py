#User function Template for python3

from collections import Counter

class Solution:
    def isSubset(self, a, b):
       
        count_a = Counter(a)
        
       
        for x in b:
            if count_a[x] > 0:
                count_a[x] -= 1
            else:
                
                return False
                
        return True
    
    
    
