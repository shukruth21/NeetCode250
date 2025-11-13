class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        area = 0
        while l<r:
            ar=min(nums[l],nums[r])*(r-l)
            area=max(area,ar)
            if(nums[l]>nums[r]):
                r-=1
            else:
                l+=1
        return area
