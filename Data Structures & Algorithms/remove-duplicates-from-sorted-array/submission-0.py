class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Brute force TC->O(NlogN+N) SC->O(N)
        seen=set()
        index=0

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index]=num
                index+=1
        return index
        