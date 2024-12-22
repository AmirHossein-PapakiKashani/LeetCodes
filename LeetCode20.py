class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        if len(s) == 1 :
            return False
        for i in s :
            if i in "({[":
               myStack.append(i)
            elif i in ")}]" and len(myStack) > 0: 
                last = myStack[len(myStack)-1]
                if i == ')' and last == '(':
                   myStack.pop()
                elif i == '}' and last == '{':
                   myStack.pop()
                elif i == ']' and last == '[':
                    myStack.pop()
                else :
                    return False
            else:
                return False
        if len(myStack) > 0 :
            return False
        return True
a = Solution()
print(a.isValid("){"))