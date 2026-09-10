class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = []
        def b(curr):
            if len(curr)==len(nums):
                l.append(curr.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in curr :
                    curr.append(nums[i])
                    b(curr)
                    curr.pop()
        b([])    
        return l 
        