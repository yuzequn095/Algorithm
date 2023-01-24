# Insertion and deletion

## LeetCode
- 450.Delete Node in a BST
- 701.Insert into a Binary Search Tree

### 450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:
<img src="../../../static/450-1.jpg">  
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```
<img src="../../../static/450-2.jpg">

Example 2:

```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

Example 3:

```
Input: root = [], key = 0
Output: []
``` 

Constraints:

- The number of nodes in the tree is in the range [0, 104].
- -105 <= Node.val <= 105
- Each node has a unique value.
- root is a valid binary search tree.
- -105 <= key <= 105

#### Solution
```
/*
 * 1/24/2023
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
    TreeNode deleteNode(TreeNode root, int key) {

        if (root == null) return null;

        if (root.val == key) {
            // if any subtree is null, just return the another one
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            
            // replace the current node with mini node in right subtree
            TreeNode minNode = getMin(root.right);
            // delete the mini node in right subtree
            root.right = deleteNode(root.right, minNode.val);
            // replace
            minNode.left = root.left;
            minNode.right = root.right;
            root = minNode;
        } else if (root.val > key) { // search left substree
            root.left = deleteNode(root.left, key);
        } else if (root.val < key) { // search right subtree
            root.right = deleteNode(root.right, key);
        }
        return root;
    }

    TreeNode getMin(TreeNode node) {
        // find the minimum node in left subtree
        while (node.left != null) node = node.left;
        return node;
    }

}
```

### 701. Insert into a Binary Search Tree
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


Example 1:

<img src="../../static/701-1.jpg">

```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:
```
<img src="../../static/701-2.jpg>

Example 2:
```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

Example 3:
```
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
```

Constraints:
- The number of nodes in the tree will be in the range [0, 104].
- -108 <= Node.val <= 108
- All the values Node.val are unique.
- -108 <= val <= 108
- It's guaranteed that val does not exist in the original BST.

#### Solution
```
/*
 * 1/24/2023
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
    TreeNode insertIntoBST(TreeNode root, int val) {

        // insert
        if (root == null) return new TreeNode(val);

        // if (root.val == val) - duplciate node

        // locate where to insert
        if (root.val < val) 
            root.right = insertIntoBST(root.right, val);
        if (root.val > val) 
            root.left = insertIntoBST(root.left, val);
            
        return root;
    }
}
```