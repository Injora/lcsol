class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        candidates.sort()
        def b(i,t,curr):
            if t == 0 :
                l.append(curr.copy())
                return
            if i==len(candidates) or t<0 :
                return
            curr.append(candidates[i])
            b(i+1,t-candidates[i],curr)
            curr.pop()
            j=i+1
            while j<len(candidates) and candidates[i]== candidates[j]:
                j+=1
            b(j,t,curr)
        b(0,target,[])
        return l
        