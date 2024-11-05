class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dictWord1 = dict.fromkeys(set(word1), 0)
        dictWord2 = dict.fromkeys(set(word2), 0)
        if(len(word1) != len(word2)):
            return False
        if(set(word1) != set(word2)):
            return False
        for i in range(len(word1)):
            if(word1[i] in list(dictWord1.keys())):
                dictWord1[f"{word1[i]}"] += 1 
            if(word2[i] in list(dictWord2.keys())):
                dictWord2[f"{word2[i]}"] += 1 
        if(sorted(list(dictWord1.values())) == sorted(list(dictWord2.values()))):
            return True
        return False