class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str=str(x)
        # print(num_str)
        # print(type(num_str))
        reverse_str=num_str[::-1]
        # print(reverse_str)

        if num_str==reverse_str:
            return True
        else:
            return False
        

test=Solution()
y=test.isPalindrome(121)