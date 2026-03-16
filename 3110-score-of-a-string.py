# LeetCode 3110 - Score of a String
# Author: Balaji_dev3

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            temp = abs(ord(s[i]) - ord(s[i+1]))
            ans += temp
        return ans
