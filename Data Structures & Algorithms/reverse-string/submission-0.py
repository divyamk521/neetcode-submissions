class Solution:
    def reverseString(self, s: List[str]) -> None:
        #Brute force TC->O(N) SC->O(N)
        tmp=s[::-1]

        for i in range(len(s)):
            s[i]=tmp[i]
        