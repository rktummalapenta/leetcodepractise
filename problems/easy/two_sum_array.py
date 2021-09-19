"""
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

"""

from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = len(numbers)
        result = []

        def binarySearch(nums: List[int], target: int) -> int:

            l = 0
            r = len(nums) - 1

            while l <= r:

                mid = (l+r)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return -1

        for i in range(l):

            out = target - numbers[i]

            search = binarySearch(numbers[i+1:], out)

            if search != -1:
                ind = i+1+search
                result.append(i+1)
                result.append(ind+1)
                break

        return result

    def twoSum11(self, nums: List[int], target:int) -> List[int]:

        l = 0
        r = len(nums) - 1

        while l < r:

            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1



class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        l = len(numbers)
        result = []

        for i in range(l):

            out = target - numbers[i]
            if out in numbers[i+1:]:
                ind = numbers.index(out, i+1, l)
                result.append(i+1)
                result.append(ind+1)

        return result




a = Solution()

numbers = [5,25,75]
target = 100

print(a.twoSum11(numbers, target))






