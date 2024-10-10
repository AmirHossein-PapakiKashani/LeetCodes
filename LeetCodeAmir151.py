class Solution:
    def reverseWords(self, s):
        ss=s.split()
        return ' '.join(ss[::-1])