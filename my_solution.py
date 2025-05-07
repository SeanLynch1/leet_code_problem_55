
from typing import List
class Solution:
    
    
    
    def loop(self, pointer, nums, visited_indices):
        
        visited_indices[pointer] = True
        
        jump_power = nums[pointer]
        print(f"index {pointer} :", nums[pointer])
            
            
        if jump_power == 0:
            print(f"index {pointer} can not jump further as jump power is stuck at :", nums[pointer])
            return False
                
        for j in range(1, jump_power + 1):
            print(f"attempting with jump power of:  {j}")

            pointer += 1
                    
            # if last index
            if pointer >= len(nums) - 1:
                print(f"index = {pointer}, has reached the end of the array")
                return True
            
            outcome = False
            
            if pointer not in visited_indices:
                outcome = self.loop(pointer, nums, visited_indices)
            
            if outcome == True or j == jump_power:
                return outcome
            

    def canJump(self, nums: List[int]) -> bool:
        jump_power = 0
        pointer = 0
        
        visited_indices = {}
        
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        
        outcome = False
        
        outcome = self.loop(pointer, nums, visited_indices)
        if outcome == True:
            return True
        
        return outcome
        

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
    
    
    
