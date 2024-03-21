class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = {} # Map Storing : sorted_str : index
        ans = [] # List[List[str]]

        # Loop throug the strings
        for s in strs:
            # Sort the strings
            sorted_str = ''.join(sorted(s))
            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
            else:
                mp[sorted_str] = len(ans)
                ans.append([s])
        
        return ans
