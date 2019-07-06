class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest = ""
        
        for i in range(len(s)):
            # odd
            self.findPalindrom(s, i, i)  
            # even
            self.findPalindrom(s, i, i+1)
            
        return self.longest
    
    def findPalindrom(self, s, left, right):
        while not(left < 0 or right >= len(s) or s[left] != s[right]):
            left -= 1
            right += 1
        self.longest = max(self.longest, s[left+1:right], key=len)