class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000

        }
        # for key,value in roman.items():
        #     print(key,value)
        total=0
        for i in range(len(s)):
            # print(roman[s[i + 1]])
            if i<len(s)-1 and roman[s[i]] < roman[s[i + 1]]:
                print(f"s[i]-{roman[s[i]]}")
               
                total-=roman[s[i]]
                # print(total)
            else:
                
                total+=roman[s[i]]
                # print(f"{roman[s[i]]}")
                # print(total)
        return total
s=Solution()
roman=s.romanToInt("XX")
# print(roman)


