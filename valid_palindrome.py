
# Solution 1. Uses lots of memory but pretty fast
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mp = {} # index: key
        count = 0
        for c in s:
            if c.isalpha() or c.isnumeric():
                mp[count] = c.lower()
                count += 1
    
        count = 0
        for i in range(len(mp) - 1, -1, -1):
            if mp[i] != mp[count]:
                return False
            count += 1

        return True

# Solution 2: Not as fast but way more memory efficient
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        string = ''
        for c in s:
            if c.isalpha() or c.isnumeric():
                string += c.lower()

        return (string == string[::-1])