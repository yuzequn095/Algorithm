# Elements of the greedy strategy

## LeetCode Problems
- 45.Jump Game II
- 55.Jump Game
- 253.Meeting Rooms II
- 435.Non-overlapping Intervals
- 452.Minimum Number of Arrows to Burst Balloons
- 1024.Video Stitching

### 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: nums = [2,3,0,1,4]
Output: 2
``` 

Constraints:

- 1 <= nums.length <= 104
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1]

#### Solution - DP
```
class Solution {
public:
    vector<int> memo;

    int jump(vector<int>& nums) {
        int n = nums.size();

        memo = vector<int>(n, n);
        return dp(nums, 0);
    }

    int dp(vector<int>& nums, int p) {
        int n = nums.size();
        // base case
        if (p >= n - 1) {
            return 0;
        }

        if (memo[p] != n) {
            return memo[p];
        }
        int steps = nums[p];

        for (int i = 1; i <= steps; i++) {
            int subProblem = dp(nums, p + i);
            memo[p] = min(memo[p], subProblem + 1);
        }
        return memo[p];
    }
};
```

#### Solution - Greedy
```
int jump(vector<int>& nums) {
    int n = nums.size();
    int end = 0, farthest = 0;
    int jumps = 0;
    for (int i = 0; i < n - 1; i++) {
        farthest = max(nums[i] + i, farthest);
        if (end == i) {
            jumps++;
            end = farthest;
        }
    }
    return jumps;
}
```

### 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
``` 

Constraints:

- 1 <= nums.length <= 104
- 0 <= nums[i] <= 105

#### Solution
```
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int farthest = 0;

        for (int i = 0; i < n - 1; i++) {
            // try farthest distance
            farthest = Math.max(farthest, i + nums[i]);
            // stuck at 0
            if (farthest <= i) return false;
        }

        return farthest >= n - 1;
    }
}
```

### 253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

Example 2:
```
Input: intervals = [[7,10],[2,4]]
Output: 1
``` 

Constraints:

- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

#### Solution
```
class Solution {
    int minMeetingRooms(int[][] meetings) {
        int n = meetings.length;
        int[] begin = new int[n];
        int[] end = new int[n];
        for(int i = 0; i < n; i++) {
            begin[i] = meetings[i][0];
            end[i] = meetings[i][1];
        }
        Arrays.sort(begin);
        Arrays.sort(end);

        int count = 0;

        int res = 0, i = 0, j = 0;
        while (i < n && j < n) {
            if (begin[i] < end[j]) {
                count++;
                i++;
            } else {
                count--;
                j++;
            }
            res = Math.max(res, count);
        }

        return res;
    }
}
```

### 435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

Example 2:
```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

Example 3:
```
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
``` 

Constraints:
- 1 <= intervals.length <= 105
- intervals[i].length == 2
- -5 * 104 <= starti < endi <= 5 * 104

#### Solution
```
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int n = intervals.length;
        return n - intervalSchedule(intervals);
    }

    public int intervalSchedule(int[][] intvs) {
        if (intvs.length == 0) return 0;

        Arrays.sort(intvs, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[1] - b[1];
            }
        });

        int count = 1;

        int x_end = intvs[0][1];
        for (int[] interval : intvs) {
            int start = interval[0];
            if (start >= x_end) {
                count++;
                x_end = interval[1];
            }
        }
        return count;
    }
}
```


### 452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:
```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

Example 2:
```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
```

Example 3:
```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
``` 

Constraints:
- 1 <= points.length <= 105
- points[i].length == 2
- -231 <= xstart < xend <= 231 - 1

#### Solution
```
class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;

        Arrays.sort(points, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[1] - b[1];
            }
        });

        int count = 1;

        int x_end = points[0][1];
        for (int[] interval : points) {
            int start = interval[0];
            if (start > x_end) {
                count++;
                x_end = interval[1];
            }
        }
        return count;
    }
}
```

### 1024. Video Stitching

You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.

Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.

 

Example 1:
```
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
```

Example 2:
```
Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
```

Example 3:
```
Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
Output: 3
Explanation: We can take clips [0,4], [4,7], and [6,9].
``` 

Constraints:
- 1 <= clips.length <= 100
- 0 <= starti <= endi <= 100
- 1 <= time <= 100

#### Solution
```
class Solution {
    public int videoStitching(int[][] clips, int T) {
        if (T == 0) return 0;

        Arrays.sort(clips, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });

        int res = 0;

        int curEnd = 0, nextEnd = 0;
        int i = 0, n = clips.length;
        while (i < n && clips[i][0] <= curEnd) {
            while (i < n && clips[i][0] <= curEnd) {
                nextEnd = Math.max(nextEnd, clips[i][1]);
                i++;
            }

            res++;
            curEnd = nextEnd;

            if (curEnd >= T) {
                return res;
            }
        }
        
        return -1;
    }
}
```