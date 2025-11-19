class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for i,n in enumerate(nums):
            if(n in dict):
                j=dict[n]
                return abs(i-j)<=k
            dict[i]=n
        return False
