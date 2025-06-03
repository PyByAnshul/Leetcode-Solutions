class Solution(object):
    def isValid(self, s):

        m = {'(' : ')', '[': ']', '{': '}'}
        stack = []
        for i in s:

            if i in m:

                stack.append(m[i])

            elif len(stack) > 0 and i == stack[-1]:
             
                stack.pop()
            else:
             
                return False
      
        return len(stack) == 0
                
a=Solution()
print(a.isValid('(([]){})'))