class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numberSet = set(nums) # Sets store unique numbers
        longest = 0

        for n in numberSet: 
            if (n - 1) not in numberSet: # Finds the first number in each sequence as there would be no number behind it
                length = 1
                while (n + length) in numberSet: # As long as the next number is in the numberSet, add 1
                    length += 1
                longest = max(longest, length) # Update the longest as we see
        
        return longest

        