class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        def b(i,curr):
            if i == len(nums):
                l.append(curr.copy())
                return
            curr.append(nums[i])
            b(i+1,curr)
            curr.pop()
            b(i+1,curr)
        b(0,[])
        return l
        