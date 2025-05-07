# My initial solution to LeetCode Problem 55: Jump Game

This turned out to be more complex than necessary—but I thought it was a cool exercise, so I’ve included it here.

  - I tackled the problem recursively and used a dictionary to track visited indices, effectively memoizing states to avoid redundant calculations. While this approach is logically correct and passes all test cases, it performs poorly in terms of time complexity—ranking in the bottom 5% of submissions on LeetCode.
  
  - Ultimately, I learned that this problem can be solved much more efficiently using a simple greedy algorithm with a single loop. A simple greedy algorithm is solved in O(n) time, it visits each index in an array at most once, making the optimal decision at each step, hoping that these choices lead to the correct output, in the most optimal way. I've included both my original (inefficient) recursive solution and the optimal iterative solution below.

## Problem Statement

You are given an integer array nums. Each element represents your maximum jump length at that position. Starting at the first index, return true if you can reach the last index, or false otherwise.

### Examples
  Input: [2, 3, 1, 1, 4]
  Output: true
  Explanation: Jump to index 1, then jump 3 steps to the last index.
  
  Input: [3, 2, 1, 0, 4]
  Output: false
  Explanation: You get stuck at index 3, which has a jump value of 0.
