class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'AEIOUaeiou'
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            if s[i] not in vowel:
                i = i + 1
            elif s[j] not in vowel:
                j = j - 1
            else:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        return ''.join(s)
        

