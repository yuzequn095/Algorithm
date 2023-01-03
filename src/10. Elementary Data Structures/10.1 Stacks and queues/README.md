## Stacks and Queues

## Stacks

### Monotonic Stack

### LeetCode - Monotonic Stack
- 316.Remove Duplicate Letters
- 1081.Smallest Subsequence of Distinct Characters

#### 316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
among all possible results.

Example 1:
```
Input: s = "bcabc"
Output: "abc"
```


Example 2:
```
Input: s = "cbacdcbc"
Output: "acdb"
```

Constraints:
```
1 <= s.length <= 104
s consists of lowercase English letters.
```

My Solution
```aidl
/*
 * Author @ Yu
 * 01-02-2023
 */
 
class Solution {
    public String removeDuplicateLetters(String s) {
        // go over the character in s to count the occurance number
        int[] count = new int[256];
        for(char c : s.toCharArray()){
            count[c]++;
        }

        Deque<Character> stack = new ArrayDeque<>();
        boolean[] visited = new boolean[256];

        // go over the character in s again
        for(char c : s.toCharArray()){

            // decrease the count
            count[c]--;

            // if visited, continue
            if(visited[c]){
                continue;
            }
        
            // check if c could build a smaller String
            while(!stack.isEmpty() && stack.peek() > c){
                // if the peel element is the only one
                if(count[stack.peek()] == 0){
                    break;
                }

                // otherwise pop the peek element from stack
                visited[stack.peek()] = false;
                stack.pop();
            }

            // push element c into stack
            stack.push(c);
            visited[c] = true;
        }
    
        // check if empty and build String
        StringBuilder sb = new StringBuilder();

        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        return sb.reverse().toString();
    }
}
```

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(N)

#### 1081. Smallest Subsequence of Distinct Characters

Given a string s, return the
lexicographically smallest

subsequence
of s that contains all the distinct characters of s exactly once.

Example 1:
```
Input: s = "bcabc"
Output: "abc"
```

Example 2:
```
Input: s = "cbacdcbc"
Output: "acdb"
```

Constraints:
```
1 <= s.length <= 1000
s consists of lowercase English letters.
```

```aidl
/*
 * Author @ Yu
 * 01-02-2023
 */
 
class Solution {
    public String smallestSubsequence(String s) {
        // go over the character in s to count the occurance number
        int[] count = new int[256];
        for(char c : s.toCharArray()){
            count[c]++;
        }

        Deque<Character> stack = new ArrayDeque<>();
        boolean[] visited = new boolean[256];

        // go over the character in s again
        for(char c : s.toCharArray()){

            // decrease the count
            count[c]--;

            // if visited, continue
            if(visited[c]){
                continue;
            }
        
            // check if c could build a smaller String
            while(!stack.isEmpty() && stack.peek() > c){
                // if the peel element is the only one
                if(count[stack.peek()] == 0){
                    break;
                }

                // otherwise pop the peek element from stack
                visited[stack.peek()] = false;
                stack.pop();
            }

            // push element c into stack
            stack.push(c);
            visited[c] = true;
        }
    
        // check if empty and build String
        StringBuilder sb = new StringBuilder();

        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        return sb.reverse().toString();      
    }
}
```

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(N)