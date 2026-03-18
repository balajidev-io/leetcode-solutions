# LeetCode 771-jewels-and-stones
# Author: Balaji_dev3

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in stones:
            if i in jewels:
                ans += 1
        return ans
