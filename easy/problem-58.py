class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(' ')
        print(s_list)
        while True:
            if ' ' in s_list:
                s_list.pop(' ')
            elif '' in s_list: 
                s_list.pop(s_list.index(''))
            else:
                break
        return len(s_list[-1])
    
a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))