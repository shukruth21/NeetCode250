class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset={nums[0]}
        for i in range(1,len(nums)):
            if (nums[i] in myset):
                return True
            else:
                myset.add(nums[i])
        return False
