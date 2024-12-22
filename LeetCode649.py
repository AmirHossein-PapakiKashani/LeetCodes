class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        RdiantList = []
        DireList = [] 
        for i in senate:
            if i == 'R':
                RdiantList.append(i)
            if i == 'D':
                DireList.append(i)
        
        if(RdiantList.count() > DireList.count()):
            return "Radiant"
        elif(RdiantList.count() < DireList.count()):
            return "Dire"
        else:
            if(senate[0] == 'R'):
                return "Radiant"
            else:
                return "Dire"