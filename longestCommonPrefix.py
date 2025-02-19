
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        # print(prefix)
        # print(strs[1:])
        # print(prefix[:-1])
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]

        return prefix
    # def longestCommonPrfx(self, strs:List[str])-> str:
    #     strs.sort() 
    #     first, last = strs[0], strs[-1]  

    #     i = 0
    #     while i < len(first) and first[i] == last[i]:  
    #         i += 1

    #         return first[:i]  


s=Solution()
print(s.longestCommonPrefix(['flower','flow','flew']))
print(s.longestCommonPrfx(['flower','flow','flew']))