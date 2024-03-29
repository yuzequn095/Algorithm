# Elements of the dynamic programming

## Leetcode problems
- 10.Regular Expression Matching
- 53.Maximum Subarray
- 72.Edit Distance
- 121.Best time to Buy and Sell Stock
- 122.Best Time to Buy and Sell Stock II
- 139.Word Break
- 140.Word Break II
- 174.Dungeon Game
- 198.House Robber
- 213.Hourse Robber II
- 309.Best Time to Buy and Sell Stock with Cooldown
- 312.Burst Balloons
- 322.Coin Change
- 337.Hourse Robber III
- 486.Predict the Winner
- 509.Fibonacci sequence
- 514.Freedom Trail
- 583.Delete Operation for Two Strings
- 651.4 Keys Keyboard
- 712.Minimum ASCII Delete Sum for Two Strings
- 714.Best Time to Buy and Sell Stock with Transaction Fee
- 787.Cheapest Flights Within k Stops
- 877.Stone Game
- 887.Super Egg Drop
- 931.Minimum Falling Path Sum

### 10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

- '.' Matches any single character.​​​​
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

Example 2:
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

Example 3:
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
``` 

Constraints:

- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

#### Solution
```
class Solution {
    /*
     * (s, i, p, j) -> first i of s and first j of p match
     * if same (s[i] == p[j] || p[j] == ".")
     *      if next j is "*"
     *          repeat 0: (s, i, p, j + 2)
     *          repeat more than 0: (s, i + 1, p, j)
     *      else 
     *          (s, i + 1, p, j + 1)
     *  else if not same
     *      if next j is "*"
     *          repeat 0: (s, i, p, j + 2)
     *      else
     *          return false
     */
    
    private Map<String, Boolean> map;
    public boolean isMatch(String s, String p) {
        map = new HashMap<>();
        return match(s, 0, p, 0);
    }
    
    public boolean match(String s, int i, String p, int j){
        int lenS = s.length(), lenP = p.length();
        
        // reach the end
        // if p reach the end, then check if s reach the end
        if(j == lenP){
            return i == lenS;
        }
        // if s reach the end, check if remain p can skip
        if(i == lenS){
            if((lenP - j) % 2 == 1){
                return false;
            }
            for(; j +  1 < lenP; j += 2){
                if(p.charAt(j + 1) != '*'){
                    return false;
                }
            }
            return true;
        }
        
        String str = s.substring(0, i + 1) + p.substring(0, j + 1);
        if(map.containsKey(str)){
            return map.get(str);
        }
        
        boolean ret = false;
        // if same
        if(s.charAt(i) == p.charAt(j) || p.charAt(j) == '.'){
            // if next j is "*"
            if(j < lenP - 1 && p.charAt(j + 1) == '*'){
                ret = match(s, i, p, j + 2) || match(s, i + 1, p, j);
            }
            // if next j is not "*", can't reapeat
            else{
                ret = match(s, i + 1, p, j + 1);
            }
        }
        
        // if not same
        else{
            // if next j is '*', repeat 0
            if(j < lenP - 1 && p.charAt(j + 1) == '*'){
                ret = match(s, i, p, j + 2);
            }
            // if not match and can't skip
            else{
                ret = false;
            }
        }
        
        map.put(str, ret);
        
        return ret;
    }
}
```

### 53. Maximum Subarray
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

Example 2:
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
``` 

Constraints:

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

#### Solution - Sliding Window
```
class Solution {
    int maxSubArray(int[] nums) {
        int left = 0, right = 0;
        int windowSum = 0, maxSum = Integer.MIN_VALUE;
        while(right < nums.length){
            windowSum += nums[right];
            right++;

            maxSum = windowSum > maxSum ? windowSum : maxSum;

            while(windowSum < 0) {
                windowSum -=  nums[left];
                left++;
            }
        }
        return maxSum;
    }
}
```

#### Solution - Dynamic Programming
```
class Solution {
    int maxSubArray(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;

        int[] dp = new int[n];
        // base case
        dp[0] = nums[0];

        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(nums[i], nums[i] + dp[i - 1]);
        }

        int res = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```
Space Optimization:
```
int maxSubArray(int[] nums) {
    int n = nums.length;
    if (n == 0) return 0;
    // base case
    int dp_0 = nums[0];
    int dp_1 = 0, res = dp_0;

    for (int i = 1; i < n; i++) {
        // dp[i] = max(nums[i], nums[i] + dp[i-1])
        dp_1 = Math.max(nums[i], nums[i] + dp_0);
        dp_0 = dp_1;
        res = Math.max(res, dp_1);
    }
    
    return res;
}
```

### 72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

Example 2:
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

Constraints:

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

#### Solution
```
class Solution {

    int[][] memo;
        
    public int minDistance(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        
        memo = new int[m][n];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        return dp(s1, m - 1, s2, n - 1);
    }

    int dp(String s1, int i, String s2, int j) {
        if (i == -1) return j + 1;
        if (j == -1) return i + 1;
        
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = dp(s1, i - 1, s2, j - 1);
        } else {
            memo[i][j] =  min(
                dp(s1, i, s2, j - 1) + 1,
                dp(s1, i - 1, s2, j) + 1,
                dp(s1, i - 1, s2, j - 1) + 1
            );
        }
        return memo[i][j];
    }

    int min(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
}

```

### 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
``` 

Constraints:

- 1 <= prices.length <= 105
- 0 <= prices[i] <= 104

#### Solution
```
class Solution {
    int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        for (int i = 0; i < n; i++) {
            if (i - 1 == -1) {
                // base case
                dp[i][0] = 0;
                dp[i][1] = -prices[i];
                continue;
            }
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
        }
        return dp[n - 1][0];
    }
}
```

#### Solution - Space Optimized
```
int maxProfit_k_1(int[] prices) {
    int n = prices.length;
    // base case: dp[-1][0] = 0, dp[-1][1] = -infinity
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        // dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        // dp[i][1] = max(dp[i-1][1], -prices[i])
        dp_i_1 = Math.max(dp_i_1, -prices[i]);
    }
    return dp_i_0;
}
```

### 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

Example 2:
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

Example 3:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
``` 

Constraints:

- 1 <= prices.length <= 3 * 104
- 0 <= prices[i] <= 104

#### Solution
```
class Solution {
    int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        for (int i = 0; i < n; i++) {
            if (i - 1 == -1) {
                // base case
                dp[i][0] = 0;
                dp[i][1] = -prices[i];
                continue;
            }
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0] - prices[i]);
        }
        return dp[n - 1][0];
    }
}
```

#### Solution - Space Optimized
```
int maxProfit_k_inf(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i]);
    }
    return dp_i_0;
}
```

### 123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

Example 2:
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
```

Example 3:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
``` 

Constraints:

- 1 <= prices.length <= 105
- 0 <= prices[i] <= 105

#### Solution
```
class Solution {
    int maxProfit(int[] prices) {
        int max_k = 2, n = prices.length;
        int[][][] dp = new int[n][max_k + 1][2];
        for (int i = 0; i < n; i++) {
            for (int k = max_k; k >= 1; k--) {
                if (i - 1 == -1) {
                    // base case
                    dp[i][k][0] = 0;
                    dp[i][k][1] = -prices[i];
                    continue;
                }
                dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
                dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);
            }
        }
    
        return dp[n - 1][max_k][0];
    }
}
```

#### Solution - Space Optimized
```
int maxProfit_k_2(int[] prices) {
    // base case
    int dp_i10 = 0, dp_i11 = Integer.MIN_VALUE;
    int dp_i20 = 0, dp_i21 = Integer.MIN_VALUE;
    for (int price : prices) {
        dp_i20 = Math.max(dp_i20, dp_i21 + price);
        dp_i21 = Math.max(dp_i21, dp_i10 - price);
        dp_i10 = Math.max(dp_i10, dp_i11 + price);
        dp_i11 = Math.max(dp_i11, -price);
    }
    return dp_i20;
}
```

### 139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2:
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

Example 3:
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
``` 

Constraints:

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

#### Solution I - Backtrack
```
class Solution {
    List<String> wordDict;
    boolean found = false;
    LinkedList<String> track = new LinkedList<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        this.wordDict = wordDict;
        backtrack(s, 0);
        return found;
    }

    void backtrack(String s, int i) {
        // base case
        if (found) {
            return;
        }
        if (i == s.length()) {
            found = true;
            return;
        }

        for (String word : wordDict) {
            int len = word.length();
            if (i + len <= s.length()
                && s.substring(i, i + len).equals(word)) {
                track.addLast(word);
                backtrack(s, i + len);
                track.removeLast();
            }
        }
    }
}

```

#### Solution II - Memo
```
class Solution {
    HashSet<String> wordDict;
    int[] memo;

    public boolean wordBreak(String s, List<String> wordDict) {
        this.wordDict = new HashSet<>(wordDict);
        this.memo = new int[s.length()];
        Arrays.fill(memo, -1);
        return dp(s, 0);
    }

    boolean dp(String s, int i) {
        // base case
        if (i == s.length()) {
            return true;
        }
        if (memo[i] != -1) {
            return memo[i] == 0 ? false : true;
        }

        for (int len = 1; i + len <= s.length(); len++) {
            String prefix = s.substring(i, i + len);
            if (wordDict.contains(prefix)) {
                boolean subProblem = dp(s, i + len);
                if (subProblem == true) {
                    memo[i] = 1;
                    return true;
                }
            }
        }
        memo[i] = 0;
        return false;
    }
}

```

### 140. Work Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:
```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

Example 2:
```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
```

Example 3:
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
``` 

Constraints:

- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.
- Input is generated in a way that the length of the answer doesn't exceed 105.

#### Solution I - Backtrack
```
class Solution {
    List<String> res = new LinkedList<>();
    LinkedList<String> track = new LinkedList<>();
    List<String> wordDict;

    public List<String> wordBreak(String s, List<String> wordDict) {
        this.wordDict = wordDict;
        backtrack(s, 0);
        return res;
    }

    void backtrack(String s, int i) {
        // base case
        if (i == s.length()) {
            res.add(String.join(" ", track));
            return;
        }

        for (String word : wordDict) {
            int len = word.length();
            if (i + len <= s.length()
                && s.substring(i, i + len).equals(word)) {
                track.addLast(word);
                backtrack(s, i + len);
                track.removeLast();
            }
        }
    }
}

```

#### Solution II - Memo
```
class Solution {
    HashSet<String> wordDict;
    List<String>[] memo;

    public List<String> wordBreak(String s, List<String> wordDict) {
        this.wordDict = new HashSet<>(wordDict);
        memo = new List[s.length()];
        return dp(s, 0);
    }


    List<String> dp(String s, int i) {
        List<String> res = new LinkedList<>();
        if (i == s.length()) {
            res.add("");
            return res;
        }
        if (memo[i] != null) {
            return memo[i];
        }
        
        for (int len = 1; i + len <= s.length(); len++) {
            String prefix = s.substring(i, i + len);
            if (wordDict.contains(prefix)) {
                List<String> subProblem = dp(s, i + len);
                for (String sub : subProblem) {
                    if (sub.isEmpty()) {
                        res.add(prefix);
                    } else {
                        res.add(prefix + " " + sub);
                    }
                }
            }
        }
        memo[i] = res;
        
        return res;
    }
}

```

### 174. Dungeon Game

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:

<img src="/../../static/174-1.jpg">
```
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
```

Example 2:

```
Input: dungeon = [[0]]
Output: 1
``` 

Constraints:

- m == dungeon.length
- n == dungeon[i].length
- 1 <= m, n <= 200
- -1000 <= dungeon[i][j] <= 1000

#### Solution
```
class Solution {
    public int calculateMinimumHP(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        memo = new int[m][n];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return dp(grid, 0, 0);
    }

    int[][] memo;

    int dp(int[][] grid, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;
        // base case
        if (i == m - 1 && j == n - 1) {
            return grid[i][j] >= 0 ? 1 : -grid[i][j] + 1;
        }
        if (i == m || j == n) {
            return Integer.MAX_VALUE;
        }
        
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        
        int res = Math.min(
                dp(grid, i, j + 1),
                dp(grid, i + 1, j)
            ) - grid[i][j];
        
        memo[i][j] = res <= 0 ? 1 : res;

        return memo[i][j];
    }
}
```

### 188. Best Time to Buy and Sell Stock IV
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

Example 2:
```
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
``` 

Constraints:

- 1 <= k <= 100
- 1 <= prices.length <= 1000
- 0 <= prices[i] <= 1000

#### Solution
```
class Solution {
    int maxProfit(int max_k, int[] prices) {
        int n = prices.length;
        if (n <= 0) {
            return 0;
        }
        if (max_k > n / 2) {
            return maxProfit_k_inf(prices);
        }

        // base case：
        // dp[-1][...][0] = dp[...][0][0] = 0
        // dp[-1][...][1] = dp[...][0][1] = -infinity
        int[][][] dp = new int[n][max_k + 1][2];
        // k = 0 时的 base case
        for (int i = 0; i < n; i++) {
            dp[i][0][1] = Integer.MIN_VALUE;
            dp[i][0][0] = 0;
        }

        for (int i = 0; i < n; i++) 
            for (int k = max_k; k >= 1; k--) {
                if (i - 1 == -1) {
                    // 处理 i = -1 时的 base case
                    dp[i][k][0] = 0;
                    dp[i][k][1] = -prices[i];
                    continue;
                }
                dp[i][k][0] = Math.max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
                dp[i][k][1] = Math.max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);     
            }
        return dp[n - 1][max_k][0];
    }

    int maxProfit_k_inf(int[] prices) {
        int n = prices.length;
        int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int temp = dp_i_0;
            dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
            dp_i_1 = Math.max(dp_i_1, temp - prices[i]);
        }
        return dp_i_0;
    }
}
```

### 312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:
```
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

Example 2:
```
Input: nums = [1,5]
Output: 10
``` 

Constraints:

- n == nums.length
- 1 <= n <= 300
- 0 <= nums[i] <= 100

#### Solution
```
class Solution {
    int maxCoins(int[] nums) {
        int n = nums.length;
        
        // add dummy balloons at the head & tail
        int[] points = new int[n + 2];
        points[0] = points[n + 1] = 1;
        for (int i = 1; i <= n; i++) {
            points[i] = nums[i - 1];
        }

        // base case
        int[][] dp = new int[n + 2][n + 2];
        
        // calculate all child cases
        for (int i = n; i >= 0; i--) {
            for (int j = i + 1; j < n + 2; j++) {
                // last balloons to burst
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.max(
                        dp[i][j], 
                        dp[i][k] + dp[k][j] + points[i]*points[j]*points[k]
                    );
                }
            }
        }
        return dp[0][n + 1];
    }
}
```

### 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

Example 2:
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
``` 

Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

#### Solution - Top Down
```
class Solution {
    private int[] memo;

    public int rob(int[] nums) {
        memo = new int[nums.length];
        Arrays.fill(memo, -1);
        return dp(nums, 0);
    }

    private int dp(int[] nums, int start) {
        if (start >= nums.length) {
            return 0;
        }
        if (memo[start] != -1) return memo[start];
        
        int res = Math.max(dp(nums, start + 1), nums[start] + dp(nums, start + 2));
        memo[start] = res;
        return res;
    }

}
```

#### Solution - Down Top
```
 int rob(int[] nums) {
    int n = nums.length;
    // base case: dp[n] = 0
    int[] dp = new int[n + 2];
    for (int i = n - 1; i >= 0; i--) {
        dp[i] = Math.max(dp[i + 1], nums[i] + dp[i + 2]);
    }
    return dp[0];
}

```

#### Solution - Down Top Optimization
```
int rob(int[] nums) {
    int n = nums.length;
    int dp_i_1 = 0, dp_i_2 = 0;
    int dp_i = 0; 
    for (int i = n - 1; i >= 0; i--) {
        dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
        dp_i_2 = dp_i_1;
        dp_i_1 = dp_i;
    }
    return dp_i;
}

```

#### 213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

Example 2:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

Example 3:
```
Input: nums = [1,2,3]
Output: 3
``` 

Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

#### Solution
```
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(robRange(nums, 0, n - 2), 
                        robRange(nums, 1, n - 1));
    }

    int robRange(int[] nums, int start, int end) {
        int n = nums.length;
        int dp_i_1 = 0, dp_i_2 = 0;
        int dp_i = 0;
        for (int i = end; i >= start; i--) {
            dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
            dp_i_2 = dp_i_1;
            dp_i_1 = dp_i;
        }
        return dp_i;
    }

}
```

#### 309.Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:
```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

Example 2:
```
Input: prices = [1]
Output: 0
``` 

Constraints:

- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000

#### Solution
```
class Solution {
    int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        for (int i = 0; i < n; i++) {
            if (i - 1 == -1) {
                // base case 1
                dp[i][0] = 0;
                dp[i][1] = -prices[i];
                continue;
            }
            if (i - 2 == -1) {
                // base case 2
                dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
                // base case
                dp[i][1] = Math.max(dp[i-1][1], -prices[i]);
                //   dp[i][1] 
                // = max(dp[i-1][1], dp[-1][0] - prices[i])
                // = max(dp[i-1][1], 0 - prices[i])
                // = max(dp[i-1][1], -prices[i])
                continue;
            }
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i-1][1], dp[i-2][0] - prices[i]);
        }
        return dp[n - 1][0];
    }
}
```

#### Solution - Space Optimized
```
int maxProfit_with_cool(int[] prices) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    int dp_pre_0 = 0; // 代表 dp[i-2][0]
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, dp_pre_0 - prices[i]);
        dp_pre_0 = temp;
    }
    return dp_i_0;
}
```

### 322. Coin Change
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

### 337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:
<img src="/static/337-1.jpg">
```
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

Example 2:
<img src="/static/337-2.jpg">
```
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
``` 

Constraints:

- The number of nodes in the tree is in the range [1, 104].
- 0 <= Node.val <= 104

#### Solution
```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Map<TreeNode, Integer> memo = new HashMap<>();
    public int rob(TreeNode root) {
        if (root == null) return 0;
        if (memo.containsKey(root)) 
            return memo.get(root);
        int do_it = root.val
            + (root.left == null ? 
                0 : rob(root.left.left) + rob(root.left.right))
            + (root.right == null ? 
                0 : rob(root.right.left) + rob(root.right.right));
        int not_do = rob(root.left) + rob(root.right);
        
        int res = Math.max(do_it, not_do);
        memo.put(root, res);
        return res;
    }

}
```

#### Solution - Space Optimization
```
int rob(TreeNode root) {
    int[] res = dp(root);
    return Math.max(res[0], res[1]);
}

int[] dp(TreeNode root) {
    if (root == null)
        return new int[]{0, 0};
    int[] left = dp(root.left);
    int[] right = dp(root.right);
    int rob = root.val + left[0] + right[0];
    int not_rob = Math.max(left[0], left[1])
                + Math.max(right[0], right[1]);
    
    return new int[]{not_rob, rob};
}

```

### 486. Predict the Winner

You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

 

Example 1:
```
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
```

Example 2:
```
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
```

Constraints:

- 1 <= nums.length <= 20
- 0 <= nums[i] <= 107

#### Solution
```
class Solution {
    // first pick or second pick
    class Pair {
        int fir, sec;
        Pair(int fir, int sec) {
            this.fir = fir;
            this.sec = sec;
        }
    }

    public boolean predictTheWinner(int[] nums) {
        // if first win, then return true
        return stoneGame(nums) >= 0;
    }

    int stoneGame(int[] piles) {
        int n = piles.length;

        Pair[][] dp = new Pair[n][n];
        for (int i = 0; i < n; i++) 
            for (int j = i; j < n; j++)
                dp[i][j] = new Pair(0, 0);

        // base case, if only one number to pick
        for (int i = 0; i < n; i++) {
            dp[i][i].fir = piles[i];
            dp[i][i].sec = 0;
        }

        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                // pick one end
                int left = piles[i] + dp[i+1][j].sec;
                int right = piles[j] + dp[i][j-1].sec;
                // update fir and sec
                if (left > right) {
                    dp[i][j].fir = left;
                    dp[i][j].sec = dp[i+1][j].fir;
                } else {
                    dp[i][j].fir = right;
                    dp[i][j].sec = dp[i][j-1].fir;
                }
            }
        }
        Pair res = dp[0][n-1];
        return res.fir - res.sec;
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

### 514. Freedom Trail

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
 
Example 1:

<img src="../../static/../../static/514-1.jpg">

```
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
```

Example 2:

```
Input: ring = "godding", key = "godding"
Output: 13
``` 

Constraints:

- 1 <= ring.length, key.length <= 100
- ring and key consist of only lower case English letters.
- It is guaranteed that key could always be spelled by rotating ring.

#### Solution
```
class Solution {
    // char - all of the index
    HashMap<Character, List<Integer>> charToIndex = new HashMap<>();
    int[][] memo;

    public int findRotateSteps(String ring, String key) {
        int m = ring.length();
        int n = key.length();
        // init as 0
        memo = new int[m][n];

        // store the char with the index
        for (int i = 0; i < ring.length(); i++) {
            char c = ring.charAt(i);
            if (!charToIndex.containsKey(c)) {
                charToIndex.put(c, new LinkedList<>());
            }
            charToIndex.get(c).add(i);
        }

        return dp(ring, 0, key, 0);
    }

    // the minimum move from ring[i] to key[j]
    int dp(String ring, int i, String key, int j) {
        // base case - key finished
        if (j == key.length()) return 0;

        // check memo
        if (memo[i][j] != 0) return memo[i][j];
        
        int n = ring.length();
    
        int res = Integer.MAX_VALUE;

        // check each possible char
        for (int k : charToIndex.get(key.charAt(j))) {
            // the move number
            int delta = Math.abs(k - i);
            // direction (clockwise or anti-clockwise)
            delta = Math.min(delta, n - delta);
            // move to k and continue
            int subProblem = dp(ring, k, key, j + 1);
            // +1 for button and keep the minimum one
            res = Math.min(res, 1 + delta + subProblem);
        }
        
        memo[i][j] = res;
        return res;
    }
}

```

### 583.Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
```
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```

Example 2:
```
Input: word1 = "leetcode", word2 = "etco"
Output: 4
``` 

Constraints:

- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.

#### Solution
```
class Solution {
    public int minDistance(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int lcs = longestCommonSubsequence(s1, s2);
        return m - lcs + n - lcs;
    }

    public int longestCommonSubsequence(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        return dp[m][n];
    }
}
```

### 651. 4 Keys Keyboard

Imagine you have a special keyboard with the following keys:

- A: Print one 'A' on the screen.
- Ctrl-A: Select the whole screen.
- Ctrl-C: Copy selection to buffer.
- Ctrl-V: Print buffer on screen appending it after what has already been printed.

Given an integer n, return the maximum number of 'A' you can print on the screen with at most n presses on the keys.

 

Example 1:

> Input: n = 3
> Output: 3
> Explanation: We can at most get 3 A's on screen by pressing the following key sequence:
> A, A, A


Example 2:

> Input: n = 7
> Output: 9
> Explanation: We can at most get 9 A's on screen by pressing following key sequence:
> A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
 

Constraints:

- 1 <= n <= 50

#### Solution
```
class Solution {
    public int maxA(int N) {
        int[] dp = new int[N + 1];
        dp[0] = 0;
        for (int i = 1; i <= N; i++) {
            // press A
            dp[i] = dp[i - 1] + 1;
            for (int j = 2; j < i; j++) {
                // C-A & C-C dp[j-2]，C-V i - j times
                dp[i] = Math.max(dp[i], dp[j - 2] * (i - j + 1));
            }
        }
        
        return dp[N];
    }
}
```

### 712. Minimum ASCII Delete Sum for Two Strings
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:
```
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```

Example 2:
```
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
``` 

Constraints:

- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of lowercase English letters.

#### Solution
```
class Solution {
    int memo[][];
   
    int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        
        memo = new int[m][n];
        for (int[] row : memo) 
            Arrays.fill(row, -1);
        
        return dp(s1, 0, s2, 0);
    }


    int dp(String s1, int i, String s2, int j) {
        int res = 0;
        // base case
        if (i == s1.length()) {
            for (; j < s2.length(); j++)
                res += s2.charAt(j);
            return res;
        }
        if (j == s2.length()) {
            for (; i < s1.length(); i++)
                res += s1.charAt(i);
            return res;
        }
        
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = dp(s1, i + 1, s2, j + 1);
        } else {
            memo[i][j] = Math.min(
                s1.charAt(i) + dp(s1, i + 1, s2, j),
                s2.charAt(j) + dp(s1, i, s2, j + 1)
            );
        }
        return memo[i][j];
    }
}
```

### 714.Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:
```
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

Example 2:
```
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
``` 

Constraints:

- 1 <= prices.length <= 5 * 104
- 1 <= prices[i] < 5 * 104
- 0 <= fee < 5 * 104

#### Solution
```
class Solution {
    int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        for (int i = 0; i < n; i++) {
            if (i - 1 == -1) {
                // base case
                dp[i][0] = 0;
                dp[i][1] = -prices[i] - fee;
                //   dp[i][1]
                // = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
                // = max(dp[-1][1], dp[-1][0] - prices[i] - fee)
                // = max(-inf, 0 - prices[i] - fee)
                // = -prices[i] - fee
                continue;
            }
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee);
        }
        return dp[n - 1][0];
    }
}
```

#### Solution - Space Optimized
```
int maxProfit_with_fee(int[] prices, int fee) {
    int n = prices.length;
    int dp_i_0 = 0, dp_i_1 = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
        int temp = dp_i_0;
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        dp_i_1 = Math.max(dp_i_1, temp - prices[i] - fee);
    }
    return dp_i_0;
}
```

### 787. Cheapest Flights Within k Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:
<img src="../../static/787-1.png">
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```


Example 2:
<img src="../../static/787-2.png">
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

Example 3:
<img src="../../static/787-3.png">
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
```

Constraints:

- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 104
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst


#### Solution - DP
```
class Solution {
    int src, dst;
    HashMap<Integer, List<int[]>> indegree;
    int[][] memo;

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        K++;
        this.src = src;
        this.dst = dst;

        memo = new int[n][K + 1];
        for (int[] row : memo) {
            Arrays.fill(row, -888);
        }
            
        // set up indegree map [s1, (s0, price)]
        indegree = new HashMap<>();
        for (int[] f : flights) {
            int from = f[0];
            int to = f[1];
            int price = f[2];
            indegree.putIfAbsent(to, new LinkedList<>());
            indegree.get(to).add(new int[] {from, price});
        }
        
        return dp(dst, K);
    }

    // the cheapest from src to s within k 
    int dp(int s, int k) {
        // find the src, no more cost
        if (s == src) {
            return 0;
        }
        // out of the k stops
        if (k == 0) {
            return -1;
        }

        if (memo[s][k] != -888) {
            return memo[s][k];
        }

        int res = Integer.MAX_VALUE;
        if (indegree.containsKey(s)) {
            for (int[] v : indegree.get(s)) {
                int from = v[0];
                int price = v[1];
                
                int subProblem = dp(from, k - 1);

                if (subProblem != -1) {
                    res = Math.min(res, subProblem + price);
                }
            }
        }
        
        
        memo[s][k] = res == Integer.MAX_VALUE ? -1 : res;
        return memo[s][k];
    }

}
```

#### Solution - Dijkstra 
```
public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
    List<int[]>[] graph = new LinkedList[n];
    for (int i = 0; i < n; i++) {
        graph[i] = new LinkedList<>();
    }
    for (int[] edge : flights) {
        int from = edge[0];
        int to = edge[1];
        int price = edge[2];
        graph[from].add(new int[]{to, price});
    }

    K++;
    return dijkstra(graph, src, K, dst);
}

class State {
    int id;
    int costFromSrc;
    int nodeNumFromSrc;

    State(int id, int costFromSrc, int nodeNumFromSrc) {
        this.id = id;
        this.costFromSrc = costFromSrc;
        this.nodeNumFromSrc = nodeNumFromSrc;
    }
}

int dijkstra(List<int[]>[] graph, int src, int k, int dst) {
    int[] distTo = new int[graph.length];
    int[] nodeNumTo = new int[graph.length];
    Arrays.fill(distTo, Integer.MAX_VALUE);
    Arrays.fill(nodeNumTo, Integer.MAX_VALUE);
    // base case
    distTo[src] = 0;
    nodeNumTo[src] = 0;

    Queue<State> pq = new PriorityQueue<>((a, b) -> {
        return a.costFromSrc - b.costFromSrc;
    });
    pq.offer(new State(src, 0, 0));

    while (!pq.isEmpty()) {
        State curState = pq.poll();
        int curNodeID = curState.id;
        int costFromSrc = curState.costFromSrc;
        int curNodeNumFromSrc = curState.nodeNumFromSrc;
        
        if (curNodeID == dst) {
            return costFromSrc;
        }
        if (curNodeNumFromSrc == k) {
            continue;
        }

        for (int[] neighbor : graph[curNodeID]) {
            int nextNodeID = neighbor[0];
            int costToNextNode = costFromSrc + neighbor[1];
            int nextNodeNumFromSrc = curNodeNumFromSrc + 1;

            if (distTo[nextNodeID] > costToNextNode) {
                distTo[nextNodeID] = costToNextNode;
                nodeNumTo[nextNodeID] = nextNodeNumFromSrc;
            }
            if (costToNextNode > distTo[nextNodeID]
                && nextNodeNumFromSrc > nodeNumTo[nextNodeID]) {
                continue;
            }
            
            pq.offer(new State(nextNodeID, costToNextNode, nextNodeNumFromSrc));
        }
    }
    return -1;
}

```

### 877. Stone Game

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

Example 1:
```
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
```

Example 2:
```
Input: piles = [3,7,2,3]
Output: true
```

Constraints:

- 2 <= piles.length <= 500
- piles.length is even.
- 1 <= piles[i] <= 500
- sum(piles[i]) is odd.

#### Solution
```
class Solution {

    // nested class for Alice and Bob
    class Player {
        int fir;
        int sec;

        public Player(int fir, int sec) {
            this.fir = fir;
            this.sec = sec;
            }
    }

    public boolean stoneGame(int[] piles) {
        
        // basic var
        int len = piles.length;

        // init 
        Player[][] mem = new Player[len][len];
        for(int i = 0; i < len; i++) {
            for(int j = i; j < len; j++) {
                mem[i][j] = new Player(0, 0);
            }
        }

        for(int i = 0; i < len; i++) {
            mem[i][i].fir = piles[i];
            mem[i][i].sec = 0;
        }

        // start
        for(int i = len - 2; i >= 0; i--) {
            for(int j = i + 1; j < len; j++) {
                // Alice choose first
                int left = piles[i] + mem[i + 1][j].sec;
                int right = piles[j] + mem[i][j - 1].sec;

                // compare
                if(left >= right) {
                    mem[i][j].fir = left;
                    mem[i][j].sec = mem[i + 1][j].fir;
                }
                else {
                    mem[i][j].fir = right;
                    mem[i][j].sec = mem[i][j - 1].fir;
                }
            }
        }

        return (mem[0][len - 1].fir - mem[0][len - 1].sec) > 0;
    }
}
```

### 887. Super Egg Drop


You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.


Example 1:
```
Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
```

Example 2:
```
Input: k = 2, n = 6
Output: 3
```

Example 3:
```
Input: k = 3, n = 14
Output: 4
``` 

Constraints:

1 <= k <= 100
1 <= n <= 104

#### Solution - TLE
```
class Solution {
    private int[][] mem;

    public int superEggDrop(int k, int n) {
        mem = new int[k + 1][n + 1]; // the minimum number of moves with k eggs and n floors
        for(int[] row : mem) {
            Arrays.fill(row, -1);
        }
        return dp(k, n);
    }

    private int dp(int k, int n) {
        // base case
        if(k == 1) {// only one egg remains, we have to go floor one by one
            return n;
        }
        if(n == 0) {// only one floor remains, we have only one choice
            return 0;
        }

        // check mem
        if(mem[k][n] != -1) {
            return mem[k][n];
        }

        int res = Integer.MAX_VALUE;

        for(int i = 1; i <= n; i++) {
            // drop at ith floor
            int tmp = Math.max(
                dp(k - 1, i - 1), // broken
                dp(k, n - i) // not broken
            ) + 1; // this move

            res = Math.min(res, tmp);
        }

        mem[k][n] = res;
        return mem[k][n];
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