from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        myStack = deque()
        
        for i in s:
            if "*" == i :
                myStack.pop()
            else:
                myStack.append(i) 
        
        return "".join(myStack)                
    
a = Solution()
print(a.removeStars("leet**cod*e"))