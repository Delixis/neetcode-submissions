class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for x in nums:
            if x not in result:
                result[x] = 1
            else:
                return True
        return False
