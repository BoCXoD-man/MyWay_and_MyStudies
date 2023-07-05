Сhapters:

- 375 [Guess Number Higher or Lower II](#guess-number-higher-or-lower-ii)
- 1480 [Running Sum of 1d Array](#running-sum-of-1d-array)
- 1672 [Richest Customer Wealth](#richest-customer-wealth)


<hr>

## Guess Number Higher or Lower II

We are playing the Guessing Game. The game will work as follows:

    I pick a number between 1 and n.
    You guess a number.
    If you guess the right number, you win the game.
    If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
    Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.

    Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

    Example 1:

    Input: n = 10
    Output: 16
    Explanation: The winning strategy is as follows:
    - The range is [1,10]. Guess 7.
        - If this is my number, your total is $0. Otherwise, you pay $7.
        - If my number is higher, the range is [8,10]. Guess 9.
            - If this is my number, your total is $7. Otherwise, you pay $9.
            - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
            - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
        - If my number is lower, the range is [1,6]. Guess 3.
            - If this is my number, your total is $7. Otherwise, you pay $3.
            - If my number is higher, the range is [4,6]. Guess 5.
                - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
                - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
                - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, the range is [1,2]. Guess 1.
                - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
                - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
    The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

    # My Decision:

```python
    class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for length in range(2, n+1):
            for start in range(1, n - length + 2):
                dp[start][start+length-1] = float('inf')
                for x in range(start, start+length):
                    cost = x + max(dp[start][x-1] if x > start else 0, 
                    dp[x+1][start+length-1] if x < start+length-1 else 0)
                    dp[start][start+length-1] = min(dp[start][start+length-1], cost)
        return dp[1][n]
```

<hr>

## Running Sum of 1d Array

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

    # My Decision:
```python
    class Solution(object):
        def runningSum(self, nums):

            """
            :type nums: List[int]
            :rtype: List[int]
            """

            result = [nums[0]]
            for i in range(1, len(nums)):
                result.append(result[i-1] + nums[i])

            return result
```

<hr>

## Richest Customer Wealth

    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

    Example 1:

    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    Explanation:
    1st customer has wealth = 1 + 2 + 3 = 6
    2nd customer has wealth = 3 + 2 + 1 = 6
    Both customers are considered the richest with a wealth of 6 each, so return 6.

    Example 2:

    Input: accounts = [[1,5],[7,3],[3,5]]
    Output: 10
    Explanation: 
    1st customer has wealth = 6
    2nd customer has wealth = 10 
    3rd customer has wealth = 8
    The 2nd customer is the richest with a wealth of 10.

    Example 3:

    Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
    Output: 17

    # My Decision:
```python
    class Solution(object):
        def maximumWealth(self, accounts):
            """
            :type accounts: List[List[int]]
            :rtype: int
            """
            result = 0

            for list_ in accounts:
                count_summ = 0
                for num in list_:
                    count_summ += num
                if count_summ > result:
                    result = count_summ

            return result
```

<hr>
