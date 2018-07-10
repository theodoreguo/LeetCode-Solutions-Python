# coding=utf-8
"""
Question:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

- Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?

Link: https://leetcode.com/problems/rotate-array/
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #  while k > 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1
        for i in range(k):
            val = nums.pop()
            nums.insert(0, val)

"""
A little important thing to be cautious:

nums[:] = nums[n-k:] + nums[:n-k] 
can't be written as:
nums = nums[n-k:] + nums[:n-k]
on the OJ.

The previous one can truly change the value of old nums, but the following one just changes its reference to a new nums 
not the value of old nums.
"""
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

"""
O(n) runtime, O(1) space

Classical 3-step array rotation:
1. reverse the first n - k elements: [4,3,2,1,5,6,7]
2. reverse the rest of them: [4,3,2,1,7,6,5]
3. reverse the entire array: [5,6,7,1,2,3,4]
"""
class Solution3(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

if __name__ == '__main__':
    a1, k1 = [1,2,3,4,5,6,7], 3
    # Solution().rotate(a1, k1)
    # print a1
    Solution2().rotate(a1, k1)
    print a1
    # Solution3().rotate(a1, k1)
    # print a1

    a2, k2 = [-1,-100,3,99], 2
    # Solution().rotate(a2, k2)
    # print a2
    Solution2().rotate(a2, k2)
    print a2
    # Solution3().rotate(a2, k2)
    # print a2
