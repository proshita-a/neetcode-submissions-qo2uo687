class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mylist = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        pairlist = sorted([nums[i],nums[j],nums[k]])
                        if pairlist not in mylist:
                            mylist.append(pairlist)
        return mylist