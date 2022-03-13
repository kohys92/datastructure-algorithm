# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


# Dynamic Programming, Kadane's Algorithm
# Intuition
#
# Whenever you see a question that asks for the maximum or minimum of something, consider Dynamic Programming as a
# possibility. The difficult part of this problem is figuring out when a negative number is "worth" keeping in a
# subarray. This question in particular is a popular problem that can be solved using an algorithm called Kadane's
# Algorithm. If you're good at problem-solving though, it's quite likely you'll be able to come up with the algorithm
# on your own. This algorithm also has a very greedy-like intuition behind it.
#
# Let's focus on one important part: where the optimal subarray begins. We'll use the following example.
#
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# We can see that the optimal subarray couldn't possibly involve the first 3 values - the overall sum of those
# numbers would always subtract from the total. Therefore, the subarray either starts at the first 4, or somewhere
# further to the right.
#
# What if we had this example though?
#
# nums = [-2,1000000000,-3,4,-1,2,1,-5,4]
#
# We need a general way to figure out when a part of the array is worth keeping.
#
# As expected, any subarray whose sum is positive is worth keeping. Let's start with an empty array, and iterate
# through the input, adding numbers to our array as we go along. Whenever the sum of the array is negative,
# we know the entire array is not worth keeping, so we'll reset it back to an empty array.
#
# However, we don't actually need to build the subarray, we can just keep an integer variable current_subarray and
# add the values of each element there. When it becomes negative, we reset it to 0 (an empty array).