class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        map = {} # value : index

        for i, n in enumerate(nums):
            if n in map:
                return True
            map[n] = i
        
        return False