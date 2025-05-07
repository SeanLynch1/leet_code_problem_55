from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True
    
    
test_case_1 = [2, 0, 0]
test_case_2 = [3,2,1,0,4]
test_case_3 = [2,3,1,1,4]


test_cases = [
              test_case_1,
              test_case_2,
              test_case_3
              ]

expected_output = [
                    True,
                    False,
                    True
                  ]

solution = Solution()
    
for i in range(len(test_cases)):
    result = solution.canJump(test_cases[i])
    print("Result output = ", result)
    if result == expected_output[i]:
        print(f"TEST {i + 1} CASE PASSED")