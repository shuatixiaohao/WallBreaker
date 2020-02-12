class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        for item in s:
            map1[item] = map1.get(item, 0) + 1
        for item in t:
            map2[item] = map2.get(item, 0) + 1
        if len(map1) != len(map2):
            return False
        for c, val in map1.items():
            if c not in map2 or map2[c] != val:
                return False
        return True
        
