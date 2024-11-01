#https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hsmp = {}

        for size in range(minSize, maxSize + 1):
            for i in range(len(s)):
                if len(set(s[i:i+size])) <= maxLetters and minSize <= len(s[i:i+size]) <= maxSize: 
                    hsmp[s[i:i+size]] = hsmp.get(s[i:i+size],0) + 1

            return max(hsmp.values()) if len(hsmp) > 0 else 0
