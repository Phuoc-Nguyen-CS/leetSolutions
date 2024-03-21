class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {} # value, index

        for i, v in enumerate(nums):
            diff = target - v
            if diff in map:
                return [i, map[diff]]
            map[v] = i
        return []
            
def test_twoSum():
    solution = Solution()

    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [1, 0]

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [2, 1]

    # Test case 3
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [1, 0]

    print("All test cases pass")

if __name__ == "__main__":
    test_twoSum()
