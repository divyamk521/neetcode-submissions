class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointers TC->O(n2) SC->O(1)
        res=[]
        nums.sort()
        n=len(nums)

        for i in range(n):
            #if the previous and present elemets are equal skip this iteration and move next
            if i >0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=n-1

            while left<right:
                total=nums[i]+nums[left]+nums[right]

                if total <0:
                    left+=1
                elif total >0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])

                    left+=1
                    right-=1
                    #skip duplicate left values
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    #skip duplicate right values
                    while left<right and nums[right]==nums[right+1]:
                        right-=1

        return res




            
