class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        end = len(strs[0])
        for i in range(1,len(strs)):
            while (strs[0][:end]!=strs[i][:end]):
                end-=1;
            if end ==0:
                return ""
        return strs[0][:end]
