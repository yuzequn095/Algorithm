## LeetCode
- 2182.Merge Nodes in Between Zeros
- 2816.Double a Number Represented as a Linked List

### 2181. Merge Nodes in Between Zeros

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Example 1:
<img src="../../../static/2181-1.png">
```
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
```

Example 2:
<img src="../../../static/2181-2.png">
```
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
``` 

Constraints:

-  The number of nodes in the list is in the range [3, 2 * 105].
- 0 <= Node.val <= 1000
- There are no two consecutive nodes with Node.val == 0.
- The beginning and end of the linked list have Node.val == 0.

#### Solution - Two Pointers
```
public class Solution {

    public ListNode mergeNodes(ListNode head) {
        // Initialize a sentinel/dummy node with the first non-zero value.
        ListNode modify = head.next;
        ListNode nextSum = modify;

        while (nextSum != null) {
            int sum = 0;
            // Find the sum of all nodes until you encounter a 0.
            while (nextSum.val != 0) {
                sum += nextSum.val;
                nextSum = nextSum.next;
            }

            // Assign the sum to the current node's value.
            modify.val = sum;
            // Move nextSum to the first non-zero value of the next block.
            nextSum = nextSum.next;
            // Move modify also to this node.
            modify.next = nextSum;
            modify = modify.next;
        }
        return head.next;
    }
}
```

#### Solution - Recursion
```
class Solution {

    public ListNode mergeNodes(ListNode head) {
        // Start with the first non-zero value.
        head = head.next;
        if (head == null) {
            return head;
        }

        // Initialize a dummy head node.
        ListNode temp = head;
        int sum = 0;
        while (temp.val != 0) {
            sum += temp.val;
            temp = temp.next;
        }

        // Store the sum in head's value.
        head.val = sum;
        // Store head's next node as the recursive result for temp node.
        head.next = mergeNodes(temp);
        return head;
    }
}
```

### 2816. Double a Number Represented as a Linked List
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.
 

Example 1:

<img src="/static/2816-1.png">

```
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
```

Example 2:

<img src="/static/2816-2.png">

```
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
``` 

Constraints:

- The number of nodes in the list is in the range [1, 104]
- 0 <= Node.val <= 9
- The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

#### Solution

1. Reversing 
```
public class Solution {
    public ListNode doubleIt(ListNode head) {
        // Reverse the linked list
        ListNode reversedList = reverseList(head);
        // Initialize variables to track carry and previous node
        int carry = 0;
        ListNode current = reversedList, previous = null;

        // Traverse the reversed linked list
        while (current != null) {
            // Calculate the new value for the current node
            int newValue = current.val * 2 + carry;
            // Update the current node's value
            current.val = newValue % 10;
            // Update carry for the next iteration
            if (newValue > 9) {
                carry = 1;
            } else {
                carry = 0;
            }
            // Move to the next node
            previous = current;
            current = current.next;
        }

        // If there's a carry after the loop, add an extra node
        if (carry != 0) {
            ListNode extraNode = new ListNode(carry);
            previous.next = extraNode;
        }

        // Reverse the list again to get the original order
        ListNode result = reverseList(reversedList);

        return result;
    }

    // Method to reverse the linked list
    public ListNode reverseList(ListNode node) {
        ListNode previous = null, current = node, nextNode;

        // Traverse the original linked list
        while (current != null) {
            // Store the next node
            nextNode = current.next;
            // Reverse the link
            current.next = previous;
            // Move to the next nodes
            previous = current;
            current = nextNode;
        }
        // Previous becomes the new head of the reversed list
        return previous;
    }
}
```

2. Stack
```
public class Solution {
    public ListNode doubleIt(ListNode head) {
        // Initialize a stack to store the values of the linked list
        Stack<Integer> values = new Stack<>();
        int val = 0;

        // Traverse the linked list and push its values onto the stack
        while (head != null) {
            values.push(head.val);
            head = head.next;
        }

        ListNode newTail = null;

        // Iterate over the stack of values and the carryover
        while (!values.isEmpty() || val != 0) {
            // Create a new ListNode with value 0 and the previous tail as its next node
            newTail = new ListNode(0, newTail);

            // Calculate the new value for the current node
            // by doubling the last digit, adding carry, and getting the remainder
            if (!values.isEmpty()) {
                val += values.pop() * 2;
            }
            newTail.val = val % 10;
            val /= 10;
        }

        // Return the tail of the new linked list
        return newTail;
    }
}
```

3. Recursion
```
public class Solution {
    // To compute twice the value of each node's value and propagate carry
    public int twiceOfVal(ListNode head) {
        // Base case: if head is null, return 0
        if (head == null) return 0;
        
        // Double the value of current node and add the result of next nodes
        int doubledValue = head.val * 2 + twiceOfVal(head.next);
        
        // Update current node's value with the units digit of the result
        head.val = doubledValue % 10;
        
        // Return the carry (tens digit of the result)
        return doubledValue / 10;
    }
    
    public ListNode doubleIt(ListNode head) {
        int carry = twiceOfVal(head);
        
        // If there's a carry, insert a new node at the beginning with the carry value
        if (carry != 0) {
            head = new ListNode(carry, head);
        }
        
        return head;
    }
}
```

4. Two Pointers
```
public class Solution {
    public ListNode doubleIt(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;

        // Traverse the linked list
        while (curr != null) {
            int twiceOfVal = curr.val * 2;

            // If the doubled value is less than 10
            if (twiceOfVal < 10) {
                curr.val = twiceOfVal;
            } 
            // If doubled value is 10 or greater
            else if (prev != null) { // other than first node
                // Update current node's value with units digit of the doubled value
                curr.val = twiceOfVal % 10;
                // Add the carry to the previous node's value
                prev.val = prev.val + 1;
            } 
            // If it's the first node and doubled value is 10 or greater
            else { // first node
                // Create a new node with carry as value and link it to the current node
                head = new ListNode(1, curr);
                // Update current node's value with units digit of the doubled value
                curr.val = twiceOfVal % 10;
            }

            // Update prev and curr pointers
            prev = curr;
            curr = curr.next;
        }
        return head;
    }
}
```

5. Single Pointer
```
public class Solution {
    public ListNode doubleIt(ListNode head) {
        // If the value of the head node is greater than 4, 
        // insert a new node at the beginning
        if (head.val > 4) {
            head = new ListNode(0, head);
        }
        
        // Traverse the linked list
        for (ListNode node = head; node != null; node = node.next) {
            // Double the value of the current node 
            // and update it with the units digit
            node.val = (node.val * 2) % 10;
            
            // If the current node has a next node 
            // and the next node's value is greater than 4,
            // increment the current node's value to handle carry
            if (node.next != null && node.next.val > 4) {
                node.val++;
            }
        }
        
        return head;
    }
}
```