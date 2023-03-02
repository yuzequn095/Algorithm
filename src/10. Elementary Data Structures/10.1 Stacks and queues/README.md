## Stacks and Queues

## Stacks

### Monotonic Stack

### LeetCode - Monotonic Stack
- 225.Implement Stack using Queues
- 232.Implement Queue using Stacks
- 316.Remove Duplicate Letters
- 1081.Smallest Subsequence of Distinct Characters

#### 225. Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

- You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:
```
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
``` 

Constraints:

- 1 <= x <= 9
- At most 100 calls will be made to push, pop, top, and empty.
- All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?

My Solution
```
/*
 * 3/1/2023
 */

class MyStack {

    Queue<Integer> q = new LinkedList<>();
    int top_elem = 0;

    public void push(int x) {
        q.offer(x);
        top_elem = x;
    }
    
    public int top() {
        return top_elem;
    }
    
    public int pop() {
        int size = q.size();
        while (size > 2) {
            q.offer(q.poll());
            size--;
        }
        top_elem = q.peek();
        q.offer(q.poll());

        return q.poll();
    }
    
    public boolean empty() {
        return q.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
```

#### 232. Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:
```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

Constraints:

- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

My Solution
```
/*
 * 3/1/2023
 */
 class MyQueue {

    private Stack<Integer> s1, s2;
    
    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    
    public void push(int x) {
        s1.push(x);
    }
    
    public int pop() {
        peek();
        return s2.pop();
    }
    
    public int peek() {
        if (s2.isEmpty())
            while (!s1.isEmpty())
                s2.push(s1.pop());
        return s2.peek();
    }
    
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```

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