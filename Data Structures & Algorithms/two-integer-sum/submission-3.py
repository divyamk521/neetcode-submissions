class Solution:
    #hashmap approach TC->O(N) SC->O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i ,num in enumerate(nums):
            needed=target-num

            if needed in hashmap:
                return[hashmap[needed],i]

            hashmap[num]=i
       