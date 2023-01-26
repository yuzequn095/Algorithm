# Randomly Built Binary Search Trees

## LeetCode
- 95.Unique Binary Search Trees II
- 96.Unique Binary Search Trees
- 105.Construct Binary Tree from Preorder and Inorder Traversal
- 106.Construct Binary Tree from Inorder and Postorder Traversal
- 654.Maximum Binary Tree
- 899.Construct Binary Tree from Preorder and Postorder Traversal

### 95. Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:

<img src="../../../static/95-1.jpg">

```
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
```

Example 2:
```
Input: n = 1
Output: [[1]]
``` 

Constraints:

- 1 <= n <= 8

#### Solution
```
/*
 * 1/26/2023
 */

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
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) return new LinkedList<>();

        return build(1, n);
    }

    List<TreeNode> build(int lo, int hi) {
        List<TreeNode> res = new LinkedList<>();

        // base case
        if (lo > hi) {
            res.add(null);
            return res;
        }

        // root 
        for (int i = lo; i <= hi; i++) {
            List<TreeNode> leftTree = build(lo, i - 1);
            List<TreeNode> rightTree = build(i + 1, hi);
            
            for (TreeNode left : leftTree) {
                for (TreeNode right : rightTree) {
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    res.add(root);
                }
            }
        }

        return res;
    }
}
```

### 96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 
Example 1:

<img src="../../../static/96-1.jpg">

```
Input: n = 3
Output: 5
```


Example 2:

```
Input: n = 1
Output: 1
``` 

Constraints:

- 1 <= n <= 19


#### Solution - Two Dimension Array
```
/*
 * 1/26/2023
*/
class Solution {
    int[][] memo;

    int numTrees(int n) {
        memo = new int[n + 1][n + 1];
        return count(1, n);
    }

    int count(int lo, int hi) {
        if (lo > hi) return 1;

        // if we calcualted, use it
        if (memo[lo][hi] != 0) {
            return memo[lo][hi];
        }

        int res = 0;
        for (int mid = lo; mid <= hi; mid++) {
            int left = count(lo, mid - 1);
            int right = count(mid + 1, hi);
            res += left * right;
        }
        
        memo[lo][hi] = res;

        return res;
    }
}

```

#### Solution - One Dimension Array
```
/*
 * 1/26/2023
 */
class Solution {
    int[] memo;

    int numTrees(int n) {
        memo = new int[n + 1];
        return count(1, n);
    }

    int count(int lo, int hi) {
        if (lo > hi) return 1;

        // if we calcualted, use it
        if (memo[hi - lo + 1] != 0) {
            return memo[hi - lo + 1];
        }

        int res = 0;
        for (int mid = lo; mid <= hi; mid++) {
            int left = count(lo, mid - 1);
            int right = count(mid + 1, hi);
            res += left * right;
        }

        memo[hi - lo + 1] = res;

        return res;
    }
}
```

### 105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

<img src="../../../static/105-1.jpg">

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

Example 2:

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

#### My Solution
```
/*
 * Author @ Yu
 * 1/3/2022
 */
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

    private Map<Integer, Integer> map;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // build hashMap to help us look up element and its index quickly
        map = new HashMap<>();
        for(int i = 0; i < inorder.length; i++){
            map.put(inorder[i], i);
        }

        // call a helper function to build tree
        // need the range in preorder and inorder
        return build(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    public TreeNode build(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd){
        // base case
        // if we have run out of the root node
        if(preStart > preEnd){
            return null;
        }

        // pick up the first element in preorder list as the root node
        int rootVal = preorder[preStart];

        // get the location for the root in inorder
        int rootInInorder = map.get(rootVal);

        // get the leftsize
        int leftSize = rootInInorder - inStart;

        // build the root
        TreeNode root = new TreeNode(rootVal);

        // build the subtree
        root.left = build(preorder, preStart + 1, preStart + leftSize, inorder, inStart, rootInInorder - 1);
        root.right = build(preorder, preStart + leftSize + 1, preEnd, inorder, rootInInorder + 1, inEnd);

        return root;
    }
}
```

### 106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 
Example 1:

<img src="../../../static/106-1.jpg">

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

Example 2:
```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

Constraints:
- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- inorder and postorder consist of unique values.
- Each value of postorder also appears in inorder.
- inorder is guaranteed to be the inorder traversal of the tree.
- postorder is guaranteed to be the postorder traversal of the tree.

#### My Solution
```
/*
 * Author @ Yu
 * 1/3/2023
 */

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

    private Map<Integer, Integer> map;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        map = new HashMap<>();

        // map the element to its index in inorder
        // to pick up the root element quickly
        for(int i = 0; i < inorder.length; i++){
            map.put(inorder[i], i);
        }

        return build(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);    
    }

    public TreeNode build(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd){
        // base case
        // if no valid root element, return null
        if(inStart > inEnd){
            return null;
        }

        // pick up the root value
        int rootVal = postorder[postEnd];

        // get the index in inorder from map
        int rootInInorder = map.get(rootVal);

        // get the right size
        int rightSize = inEnd - rootInInorder;

        // build the subtree
        TreeNode root = new TreeNode(rootVal);
        root.right = build(inorder, rootInInorder + 1, inEnd, postorder, postEnd - rightSize - 1, postEnd - 1); 
        root.left = build(inorder, inStart, rootInInorder - 1, postorder, postStart, postEnd - rightSize - 1);

        return root;
    }
}
```

### 654. Maximum Binary Tree

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

 

Example 1:

<img src="../../static/../../static/654-1.jpg">

```
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
```

Example 2:

<img src="../../static/../../static/654-2.jpg">

```
Input: nums = [3,2,1]
Output: [3,null,2,null,1]
```

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
- All integers in nums are unique.

#### My Solution
```
/*
 * Author @ Yu
 * 1/3/2023
 */
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        // use a helper function to build a tree in a range
        return build(nums, 0, nums.length - 1);
    }

    public TreeNode build(int[] nums, int start, int end){
        // if invalid
        if(start > end){
            return null;
        }

        // get the max value
        int max = Integer.MIN_VALUE;
        int index = 0;
        for(int i = start; i <= end; i++){
            if(nums[i] > max){
                max = nums[i];
                index = i;
            }
        }

        // build the tree
        TreeNode root = new TreeNode(max);
        root.left = build(nums, start, index - 1);
        root.right = build(nums, index + 1, end);

        return root;
    }
}
```

### 899. Construct Binary Tree from Preorder and Postorder Traversal
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:

<img src="../../../static/889-1.jpg">

```
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
```

Example 2:

```
Input: preorder = [1], postorder = [1]
Output: [1]
```

Constraints:
- 1 <= preorder.length <= 30
- 1 <= preorder[i] <= preorder.length
- All the values of preorder are unique.
- postorder.length == preorder.length
- 1 <= postorder[i] <= postorder.length
- All the values of postorder are unique.
- It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

#### My Solution
```
/*
 * Author @ Yu
 * 1/3/2023
 */

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

    private Map<Integer, Integer> map;

    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        map = new HashMap<>();

        // map the element to its index in postorder
        for(int i = 0; i < postorder.length; i++){
            map.put(postorder[i], i);
        }    

        return build(preorder, 0, preorder.length - 1, postorder, 0, postorder.length - 1);
    }

    public TreeNode build(int[] preorder, int preStart, int preEnd, int[] postorder, int postStart, int postEnd){

        // base case
        if(preStart > preEnd){
            return null;
        }

        if(preStart == preEnd){ //  we check this bc left root will be preStart + 1
            return new TreeNode(preorder[preStart]);
        }

        // pick up the first element from preorder as root
        int rootVal = preorder[preStart];

        // pick up the second element from preorder as the left root
        int leftRootVal = preorder[preStart + 1];

        // get the left root index in postorder
        int leftPostOrderIndex = map.get(leftRootVal);

        // get the left size
        int leftSize = leftPostOrderIndex - postStart + 1;

        // build subtree
        TreeNode root = new TreeNode(rootVal);
        root.left = build(preorder, preStart + 1, preStart + leftSize, postorder, postStart, leftPostOrderIndex);
        root.right = build(preorder, preStart + leftSize + 1, preEnd, postorder, leftPostOrderIndex + 1, postEnd - 1);

        return root;
    }
}
```