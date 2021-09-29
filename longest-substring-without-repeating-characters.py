class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Approach is sliding Window 
        
        i = 0  # current track of element
        j = 0  # sliding window size changes based on the continuous unique elements 
        maxV = 0 # Track of maximum continuous unique elements 
        setD = set([]) # set to track continuous unique elements
        
        # if the element is not present in set it will add to the set and move to the next element.  
        # if the element is present in set it will recurisively delete the set untilthe same element is found. so we are reducing the window size based on the appearance of duplicate character. basically window size is i - j         
        
        
        for i in range(len(s)):
            if s[i] not in setD: 
                setD.add(s[i])
            else: 
                while s[i] != s[j]: 
                    setD.remove(s[j])
                    j += 1 
                j += 1
            maxV = max(maxV,i - j + 1)
        return maxV
                
                
            
        
        
