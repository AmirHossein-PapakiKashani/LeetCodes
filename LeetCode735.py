class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        myStack = []
        lastElement = 0
        for i in asteroids:
            if lastElement != 0:
                if abs(i) <= abs(lastElement):
                    if i < 0 :
                        print(abs(i))
                        print(abs(lastElement))
                        pass
                    
                    else:
                        myStack.append(i)
                        lastElement = i
                # abs(i) > abs(lastElement)
                else:
                    if i < 0:
                        myStack.pop()
                        myStack.append(i)
                        lastElement = i
                    else:
                        myStack.append(i)
                        lastElement = i
            else:
                myStack.append(i)
                lastElement = i
        return myStack

a = Solution()
print(a.asteroidCollision([10,2,-5]))