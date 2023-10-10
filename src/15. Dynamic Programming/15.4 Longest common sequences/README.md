# Longest common sequences

## LeetCode
- 115.Distinct Subsequences
- 300.Longest Increasing Subsequence
- 354.Russian Doll Envelopes
- 516.Longest Palindromic Subsequence
- 1143.Longest Common Subsequence

### 115. Distinct Subsequences
Given two strings s and t, return the number of distinct 
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

Example 2:
```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

Constraints:

- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.

#### Solution 1
```
class Solution {
    int[][] memo;
    
    int numDistinct(String s, String t) {
        // set default as -1
        memo = new int[s.length()][t.length()];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return dp(s, 0, t, 0);
    }
    
    // dp(s, i, t, j) = SUM( dp(s, k + 1, t, j + 1) where k >= i and s[k] == t[j] )
    int dp(String s, int i, String t, int j) {

        // base case 1, reach the end of t
        if (j == t.length()) {
            return 1;
        }
        // base case 2, it is impossible to match t 
        if (s.length() - i < t.length() - j) {
            return 0;
        }
        // check if memo calcualted before
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        int res = 0;

        // try s substring starting from k 
        for (int k = i; k < s.length(); k++) {
            if (s.charAt(k) == t.charAt(j)) {
                // if find the same char then try the number for the following 
                res += dp(s, k + 1, t, j + 1);
            }
        }
        
        memo[i][j] = res;
        return res;
    }
}
```

#### Solution 2
```
class Solution {
    int[][] memo;
    
    int numDistinct(String s, String t) {
        memo = new int[s.length()][t.length()];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        return dp(s, 0, t, 0);
    }
    
    int dp(String s, int i, String t, int j) {
        // base case 1
        if (j == t.length()) {
            return 1;
        }
        // base case 2
        if (s.length() - i < t.length() - j) {
            return 0;
        }
        
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        int res = 0;
        
        if (s.charAt(i) == t.charAt(j)) {
            res += dp(s, i + 1, t, j + 1) + dp(s, i + 1, t, j);
        } else {
            res += dp(s, i + 1, t, j);
        }
        
        memo[i][j] = res;
        return res;
    }
}
```

### 300. Longest Increasing Subsequence
Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
``` 

Constraints:
- 1 <= nums.length <= 2500
- -104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

#### Solution
```
class Solution {
    public int lengthOfLIS(int[] nums) {
        // the LIS in ith location
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1); // 1 as self length

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) 
                    dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        
        int res = 0;
        for (int i = 0; i < dp.length; i++) {
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

### 354. Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.



Example 1:
```
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

Example 2:
```
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
``` 

Constraints:

- 1 <= envelopes.length <= 105
- envelopes[i].length == 2
- 1 <= wi, hi <= 105

#### Solution - Time Limit Exceed
```
class Solution {
    // envelopes = [[w, h], [w, h]...]
    public int maxEnvelopes(int[][] envelopes) {
        int n = envelopes.length;
        
        Arrays.sort(envelopes, new Comparator<int[]>() 
        {
            public int compare(int[] a, int[] b) {
                return a[0] == b[0] ? 
                    b[1] - a[1] : a[0] - b[0];
            }
        });
        
        int[] height = new int[n];
        for (int i = 0; i < n; i++)
            height[i] = envelopes[i][1];

        return lengthOfLIS(height);
    }

    int lengthOfLIS(int[] nums) {
        
        int[] dp = new int[nums.length];
        
        Arrays.fill(dp, 1);
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) 
                    dp[i] = Math.max(dp[i], dp[j] + 1);

            }
        }
        
        int res = 0;
        for (int i = 0; i < dp.length; i++) {
            res = Math.max(res, dp[i]);
        }
        return res;
    }

}
```

### 516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
```
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

Example 2:
```
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
``` 

Constraints:

- 1 <= s.length <= 1000
- s consists only of lowercase English letters.

#### Solution
```
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();

        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int i = 0; i < n; i++)
            dp[i][i] = 1;
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
               
                if (s[i] == s[j])
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                else
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        
        return dp[0][n - 1];
    }
};
```

### 1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

Example 2:
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

Example 3:
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
``` 

Constraints:

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

#### Solution
```
class Solution {
 
    int[][] memo;

    
    int longestCommonSubsequence(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        
        memo = new int[m][n];
        for (int[] row : memo) 
            Arrays.fill(row, -1);
        
        return dp(s1, 0, s2, 0);
    }

    int dp(String s1, int i, String s2, int j) {
        // base case
        if (i == s1.length() || j == s2.length()) {
            return 0;
        }

        if (memo[i][j] != -1) {
            return memo[i][j];
        }
      
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = 1 + dp(s1, i + 1, s2, j + 1);
        } else {
            memo[i][j] = Math.max(
                dp(s1, i + 1, s2, j),
                dp(s1, i, s2, j + 1)
            );
        }
        return memo[i][j];
    }
}
```

