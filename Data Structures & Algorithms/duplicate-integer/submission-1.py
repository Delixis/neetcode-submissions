class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for x in nums:
            result[x] = result.get(x,0) + 1
        cop = 0
        for i in result.values():
            if i > 1:
                cop += 1
        return cop > 0