class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []

        def b(i, t, curr):
            if t == 0:
                l.append(curr.copy())
                return

            if i == len(candidates) or t < 0:
                return
            curr.append(candidates[i])
            b(i, t - candidates[i], curr)
            curr.pop()
            b(i + 1, t, curr)

        b(0, target, [])

        return l