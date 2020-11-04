class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            x = nums.count(i)
            if x == 1:
                print(i)


solution = Solution()
Solution.singleNumber(self=solution, nums=[4, 1, 2, 1, 2])
