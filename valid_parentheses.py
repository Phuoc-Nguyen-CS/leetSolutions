class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        match = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        ans = []

        for c in s:
            if c in match.keys() and len(ans) != 0:
                testCase = ans.pop()
                if match[c] != testCase:
                    return False
            else:
                ans.append(c)
        
        return not ans
