# Randomized algorithms

## LeetCode
- 380.Insert Delete GetRandom O(1)
- 710.Random Pick with Blacklist


### Idea
- When we want to get random element in a same possibility and O(1), consider array
- When we want to keep valid elements together, we can swap the invalid element with the last element
- HashMap is a good tool to help us keep track of the location of element

### 380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:
```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

Constraints:

- -231 <= val <= 231 - 1
- At most 2 * 105 calls will be made to insert, remove, and getRandom.
- There will be at least one element in the data structure when getRandom is called.

#### Solution

Important HashSet method:
```
set(int index, E element)
Replaces the element at the specified position in this list with the specified element.
```

```aidl
/*
 * Author @ Yu
 * 12-23-2022
 */
 
class RandomizedSet {

    // use HashMap to bind the index and the value
    private Map<Integer, Integer> map;
    // use ArrayList to store values and shrink/expand
    List<Integer> list;
    
    public RandomizedSet() {
        map = new HashMap<>();
        list = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        // if val exist already
        if(map.containsKey(val)){
            return false; // can't insert duplicate values
        }

        // if not exist, add val into arraylist, and update index
        list.add(val);
        map.put(val, list.size() - 1);

        return true;
    }
    
    public boolean remove(int val) {
        // if val doesn't exist
        if(!map.containsKey(val)){
            return false;
        }

        // if exists, swap with the last value and remove
        int index1 = map.get(val);
        int index2 = list.size() - 1;
        int element = list.get(index2);

        list.set(index1, element);
        map.put(element, index1);

        list.remove(index2);
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        // get the random index
        Random rand = new Random();
        int index = rand.nextInt(list.size());

        System.out.println("list: " + list.size());
        System.out.println("index: " + index);
        return list.get(index);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```
### 710. Random Pick with Blacklist

You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

Implement the Solution class:

Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.
 

Example 1:

```
Input
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
Output
[null, 0, 4, 1, 6, 1, 0, 4]

Explanation
Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
                 // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
solution.pick(); // return 4
solution.pick(); // return 1
solution.pick(); // return 6
solution.pick(); // return 1
solution.pick(); // return 0
solution.pick(); // return 4
``` 

Constraints:

- 1 <= n <= 109
- 0 <= blacklist.length <= min(105, n - 1)
- 0 <= blacklist[i] < n
- All the values of blacklist are unique.
- At most 2 * 104 calls will be made to pick.

#### Solution
```
/*
 * Author @ Me
 * 12-25-2022
 */

class Solution {

    private Map<Integer, Integer> map;
    private int validSize;

    public Solution(int n, int[] blacklist) {
        map = new HashMap<>();

        // get the valid size (not in the black list)
        validSize = n - blacklist.length;
        for(int num : blacklist){
            map.put(num, -1); // use -1 to indicate this num is in blacklist
        }

        // go over the blacklist
        int last = n - 1;
        for(int num : blacklist){
            // if num has been invalid range
            if(num >= validSize){ // because num starts from 0 so we use equal here
                continue;
            }

            // swap the current num with the valid num in last
            while(map.containsKey(last)){ // if map contains last, means last is invalid
                last--;
            }

            // swap
            map.put(num, last);
            last--;
        }
    }
    
    public int pick() {
        Random rand = new Random();
        int res = rand.nextInt(validSize);

        // if the res is in the blacklist
        if(map.containsKey(res)){
            return map.get(res);
        }

        return res;
    }
}
```