### Сhapters:

- 375 [Guess Number Higher or Lower II](#guess-number-higher-or-lower-ii)
- 383 [Ransom Note](#ransom-note)
- 412 [Fizz Buzz](#fizz-buzz)
- 1342 [Number of Steps to Reduce a Number to Zero](#number-of-steps-to-reduce-a-number-to-zero)
- 1480 [Running Sum of 1d Array](#running-sum-of-1d-array)
- 1672 [Richest Customer Wealth](#richest-customer-wealth)

<hr>
<hr>

## Guess Number Higher or Lower II
Difficulty: Medium

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
<hr>

## Running Sum of 1d Array
Difficulty: Easy

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
<hr>

## Richest Customer Wealth
Difficulty: Easy

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
<hr>

## Fizz Buzz
Difficulty: Easy

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:

    Input: n = 3
    Output: ["1","2","Fizz"]

Example 2:

    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

Example 3:

    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# My Decision:
```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(n):
            str_ = ''
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                str_ += 'FizzBuzz'
            elif (i+1) % 3 == 0:
                str_ += 'Fizz'
            elif (i+1) % 5 == 0:
                str_ += 'Buzz'
            else:
                str_ += str((i+1))
            result.append(str_) 
        return result 
```
<hr>
<hr>

## Number of Steps to Reduce a Number to Zero
Difficulty: Easy

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

    Input: num = 14
    Output: 6
    Explanation: 
    Step 1) 14 is even; divide by 2 and obtain 7. 
    Step 2) 7 is odd; subtract 1 and obtain 6.
    Step 3) 6 is even; divide by 2 and obtain 3. 
    Step 4) 3 is odd; subtract 1 and obtain 2. 
    Step 5) 2 is even; divide by 2 and obtain 1. 
    Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:

    Input: num = 8
    Output: 4
    Explanation: 
    Step 1) 8 is even; divide by 2 and obtain 4. 
    Step 2) 4 is even; divide by 2 and obtain 2. 
    Step 3) 2 is even; divide by 2 and obtain 1. 
    Step 4) 1 is odd; subtract 1 and obtain 0.

Example 3:

    Input: num = 123
    Output: 12

 

Constraints:

    0 <= num <= 106

# My Decision:

```python
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
                steps += 1
            else:
                num = num -1
                steps += 1

        return steps
```
<hr>
<hr>

## Ransom Note

Difficulty: Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:

    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:

    Input: ransomNote = "aa", magazine = "aab"
    Output: true


# My Decision:

```python
# First solution example

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}

        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1
        
        for char in ransomNote:
            if char in magazine_dict and magazine_dict[char] > 0:
                magazine_dict[char] -= 1
            else:
                return False

        return True


# Second solution example
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}
    
        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1
        
        for char in ransomNote:
            if char in magazine_dict and magazine_dict[char] > 0:
                magazine_dict[char] -= 1
            else:
                return False
        return True


# The first solution came to me as soon as I read the condition of the problem, the second one came later, when I tried to optimize the solution and make it faster.
```

<hr>
<hr>

## Шаблон

Difficulty: Easy


# My Decision:

```python

```

<hr>
<hr>

## Шаблон

Difficulty: Easy


# My Decision:

```python

```