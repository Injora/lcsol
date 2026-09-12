class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append([l, r, w, i])
        arr.sort()
        starts = []

        for x in arr:
            starts.append(x[0])
        nxt = [0] * n

        for i in range(n):
            r = arr[i][1]

            nxt[i] = bisect_right(starts, r)

        dp = [[None] * 5 for _ in range(n + 1)]

        def better(a, b):

            if a[0] != b[0]:
                if a[0] > b[0]:
                    return a
                else:
                    return b

            if a[1] < b[1]:
                return a
            else:
                return b

        def solve(i, k):

            if i == n or k == 0:
                return (0, [])

            if dp[i][k] is not None:
                return dp[i][k]
            skip = solve(i + 1, k)
            score, indices = solve(nxt[i], k - 1)
            take = (
                arr[i][2] + score,
                sorted(indices + [arr[i][3]])
            )
            dp[i][k] = better(skip, take)
            return dp[i][k]
        return solve(0, 4)[1]