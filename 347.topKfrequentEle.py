#better bruteforce dictionary + sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

# brute force using dictionary
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            map[nums[i]]=1+map.get(nums[i],0)
        ans=[]
        for i in range(k):
            m=-1
            a=0
            for k,v in map.items():
                if(map[k]>m):
                    m=map[k]
                    a=k
            ans.append(a)
            map.pop(a)
        return ans
            

        
