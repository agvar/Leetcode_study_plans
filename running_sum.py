'''
1480. Running Sum of 1d Array
Easy
5.3K
269
Companies
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''


from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=0
        array_sum=[]
        for num in nums:
            running_sum+=num
            array_sum.append(running_sum)
        return array_sum

def test_cases():
    nums=[2,3,4,5]
    assert(sol.runningSum(nums))==[2, 5, 9, 14], "Incorrect Value"
    nums=[1,2,3,6]
    assert(sol.runningSum(nums))==[1,3,6,12], "Incorrect Value"
    nums=[]
    assert(sol.runningSum(nums))==[], "Incorrect Value"

if __name__=="__main__":
    sol=Solution()
    test_cases()
    print("Test cases pass")