class Solution:
    def decodeString(self, s: str) -> str:
        test = self.MakeStack(s)
        return test
    def MakeStack(self, s : list):
        myStack = []
        current_Character = ""
        current_Number = ""
        temp = ""
        for i in s :
            if i.isdigit():
                current_Number = i
            elif i.isalpha() :
                current_Character += i
                myStack.append(current_Character)
                current_Character = ""
            elif i == "[":
                myStack.append(current_Number)
                current_Number = ""
            elif i == "]":
                temp = i
                if temp == "]":
                    continue
                return myStack
a = Solution()
print(a.decodeString ( "3[a]2[bc]"))