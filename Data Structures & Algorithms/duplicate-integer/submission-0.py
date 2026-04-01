class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for n in nums:
            for i in range(nums.index(n)+1, len(nums)):
                if n == nums[i]:
                    return True;
                    break;
        return False;