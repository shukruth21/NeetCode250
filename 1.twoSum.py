class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}  # mapping value--> index
        for i,n in enumerate(nums):    #helps to get both index and value
            diff= target -n
            if(diff in prevMap):
                return [prevMap[diff],i]
            prevMap[n]=i

        
