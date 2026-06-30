class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, val in enumerate(nums):
            ch = target - val
            if ch not in result:
                result[val] = i
            else:
                return[result[ch],i]
        