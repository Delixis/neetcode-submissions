class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result_s = {}
        for x in s:
            result_s[x] = result_s.get(x,0) + 1        
        for x in t:
            result_s[x] = result_s.get(x,0) - 1
        for i in result_s.values():
            if i != 0:
                return False
        return True