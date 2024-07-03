from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        short = min(strs, key=len)
        for i, char in enumerate(short):
            for other in strs:
                if (other[i] != char):
                    return short[:i]
        return short
strs=["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))