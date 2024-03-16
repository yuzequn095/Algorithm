# Depth-first search

## LeetCode
- 46.Permutations
- 51.N-Queens
- 52.N-Queens II

### 46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

Example 3:
```
Input: nums = [1]
Output: [[1]]
``` 

Constraints:

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

#### Solution
```
class Solution {
    List<List<Integer>> res = new LinkedList<>();

    List<List<Integer>> permute(int[] nums) {
        LinkedList<Integer> track = new LinkedList<>();
        boolean[] used = new boolean[nums.length];
        
        backtrack(nums, track, used);
        return res;
    }

    void backtrack(int[] nums, LinkedList<Integer> track, boolean[] used) {
        if (track.size() == nums.length) {
            res.add(new LinkedList(track));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            track.add(nums[i]);
            used[i] = true;
            backtrack(nums, track, used);
            track.removeLast();
            used[i] = false;
        }
    }
}
```

### 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

<img src="/static/51-1.jpg">

> Input: n = 4
> Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
> Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above


Example 2:

> Input: n = 1
> Output: [["Q"]]
 

Constraints:

- 1 <= n <= 9

#### Solution
```
class Solution {
    List<List<String>> res = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append('.');
            }
            board.add(sb.toString());
        }
        backtrack(board, 0);
        return res;
    }

    void backtrack(List<String> board, int row) {
        if (row == board.size()) {
            res.add(new ArrayList<>(board));
            return;
        }
        
        int n = board.get(row).length();
        for (int col = 0; col < n; col++) {
    
            if (!isValid(board, row, col)) {
                continue;
            }

            StringBuilder sb = new StringBuilder(board.get(row));
            sb.setCharAt(col, 'Q');
            board.set(row, sb.toString());

            backtrack(board, row + 1);

            sb.setCharAt(col, '.');
            board.set(row, sb.toString());
        }
    }

    boolean isValid(List<String> board, int row, int col) {
        int n = board.size();

        for (int i = 0; i < n; i++) {
            if (board.get(i).charAt(col) == 'Q') {
                return false;
            }
        }

        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {
            if (board.get(i).charAt(j) == 'Q') {
                return false;
            }
        }

        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {
            if (board.get(i).charAt(j) == 'Q') {
                return false;
            }
        }

        return true;
    }
}

```

### 52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

<img src="/static/52.-2.jpg">

Example 1:


> Input: n = 4
> Output: 2
> Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

> Input: n = 1
> Output: 1
 

Constraints:

- 1 <= n <= 9

#### Solution
```
class Solution {
    int res = 0;

    
    public int totalNQueens(int n) {
        
        List<String> board = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append('.');
            }
            board.add(sb.toString());
        }
        backtrack(board, 0);
        return res;
    }


    void backtrack(List<String> board, int row) {

        if (row == board.size()) {
            res++;
            return;
        }

        int n = board.get(row).length();
        for (int col = 0; col < n; col++) {
            
            if (!isValid(board, row, col)) {
                continue;
            }
            
            StringBuilder sb = new StringBuilder(board.get(row));
            sb.setCharAt(col, 'Q');
            board.set(row, sb.toString());

           
            backtrack(board, row + 1);
            
            sb.setCharAt(col, '.');
            board.set(row, sb.toString());
        }
    }

    boolean isValid(List<String> board, int row, int col) {
        int n = board.size();

        for (int i = 0; i < n; i++) {
            if (board.get(i).charAt(col) == 'Q') {
                return false;
            }
        }

        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {
            if (board.get(i).charAt(j) == 'Q') {
                return false;
            }
        }

        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {
            if (board.get(i).charAt(j) == 'Q') {
                return false;
            }
        }

        return true;
    }
}

```