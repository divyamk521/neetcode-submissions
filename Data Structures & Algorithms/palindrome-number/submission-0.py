class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        res=0
        while x>0:
            digit=x%10
            res=res*10+digit
            x=x//10
        if num==res:
            return True
        else:
            return False
        