# Elements of the dynamic programming

## Leetcode problems
- 322.Coin Change
- 509.Fibonacci sequence
- 931.Minimum Falling Path Sum

### 322.Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

Example 2:
```
Input: coins = [2], amount = 3
Output: -1
```

Example 3:
```
Input: coins = [1], amount = 0
Output: 0
```

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 231 - 1
- 0 <= amount <= 104

#### Solution - Top Down
```
class Solution {
    int[] memo;

    int coinChange(int[] coins, int amount) {
        memo = new int[amount + 1];

        Arrays.fill(memo, -666);

        return dp(coins, amount);
    }

    int dp(int[] coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;

        if (memo[amount] != -666)
            return memo[amount];

        int res = Integer.MAX_VALUE;
        for (int coin : coins) {

            int subProblem = dp(coins, amount - coin);

            if (subProblem == -1) continue;

            res = Math.min(res, subProblem + 1);
        }

        memo[amount] = (res == Integer.MAX_VALUE) ? -1 : res;
        return memo[amount];
    }
}

```

### 509.Fibonacci sequence
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
```

Example 1:
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

Example 2:
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

Example 3:
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
``` 

Constraints:
- 0 <= n <= 30

#### Solution - Top Down
```
class Solution {
    public int fib(int N) {
        int[] memo = new int[N + 1];
        return dp(memo, N);
    }

    int dp(int[] memo, int n) {
        // base case
        if (n == 0 || n == 1) return n;
        if (memo[n] != 0) return memo[n];
        memo[n] = dp(memo, n - 1) + dp(memo, n - 2);
        return memo[n];
    }

}
```

#### Solution - Bottom Up
```
class Solution {
    public int fib(int N) {
        if (N == 0) return 0;
        int[] dp = new int[N + 1];
        // base case
        dp[0] = 0; dp[1] = 1;
        for (int i = 2; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[N];
    }
}
```

#### Solution - Space O(1)
```
class Solution {
    int fib(int n) {
        if (n == 0 || n == 1) {
            // base case
            return n;
        }
        // 分别代表 dp[i - 1] 和 dp[i - 2]
        int dp_i_1 = 1, dp_i_2 = 0;
        for (int i = 2; i <= n; i++) {
            // dp[i] = dp[i - 1] + dp[i - 2];
            int dp_i = dp_i_1 + dp_i_2;
            dp_i_2 = dp_i_1;
            dp_i_1 = dp_i;
        }
        return dp_i_1;
    }
}
```

### 931. Minimum Falling Path Sum
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:

<img src="../../../static/931-1.jpg">
<img src="../../../static/931-2.jpg">
<img src="../../../static/931-3.jpg">

``````
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
``````

Example 2:
<img src="../../../static/931-4.jpg">
<img src="../../../static/931-5.jpg">

``````
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
`````` 

Constraints:

- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- -100 <= matrix[i][j] <= 100


#### Solution
```
class Solution {
    int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int res = Integer.MAX_VALUE;

        memo = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], 66666);
        }
        
        for (int j = 0; j < n; j++) {
            res = Math.min(res, dp(matrix, n - 1, j));
        }
        return res;
    }

    int[][] memo;

    int dp(int[][] matrix, int i, int j) {

        if (i < 0 || j < 0 ||
            i >= matrix.length ||
            j >= matrix[0].length) {
            
            return 99999;
        }

        if (i == 0) {
            return matrix[0][j];
        }
        
        if (memo[i][j] != 66666) {
            return memo[i][j];
        }
        
        memo[i][j] = matrix[i][j] + min(
                dp(matrix, i - 1, j), 
                dp(matrix, i - 1, j - 1),
                dp(matrix, i - 1, j + 1)
            );
        return memo[i][j];
    }

    int min(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
}

```