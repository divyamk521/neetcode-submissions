class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #TC->O(N) SC->O(1)
        n=len(arr)
        ans=[0]*n
        right_max=-1

        for i in range(n-1,-1,-1):
            ans[i]=right_max
            right_max=max(arr[i],right_max)
        return ans

       

        