### 💡 My Solution
## My initial solution to LeetCode Problem 55: Jump Game turned out to be more complex than necessary—but I thought it was a cool exercise, so I’ve included it here.

- I tackled the problem recursively and used a dictionary to track visited indices, effectively memoizing states to avoid redundant calculations. While this approach is logically correct and passes all test cases, it performs poorly in terms of time complexity—ranking in the bottom 5% of submissions on LeetCode.

- Ultimately, I learned that this problem can be solved much more efficiently using a simple greedy algorithm with a single loop. I've included both my original (inefficient) recursive solution and the optimal iterative solution below.

- Sometimes, overengineering a problem is part of the learning process!
