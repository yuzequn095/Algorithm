# Kruskal and Prim

## Algorithm Pattern
Firstly, let's have a look at Union-Find, we will use it to help us valid if our graph is a valid tree.
```aidl
class UF {
    private int count;
    private int[] parent;
    private int[] size;

    public UF(int n) {
        this.count = n;
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ)
            return;

        // balance
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        
        count--;
    }

    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        return rootP == rootQ;
    }

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int count() {
        return count;
    }
}
```

Prim
```
class Prim {
    // to store cut edge
    private PriorityQueue<int[]> pq;
    // visited node
    private boolean[] inMST;
    // minimum weight
    private int weightSum = 0;
    // graph[s] - adjacent edges
    // int[]{from, to, weight}
    private List<int[]>[] graph;

    public Prim(List<int[]>[] graph) {
        this.graph = graph;
        this.pq = new PriorityQueue<>((a, b) -> {
            return a[2] - b[2];
        });
        // n nodes in graph
        int n = graph.length;
        this.inMST = new boolean[n];

        // start from 0 node
        inMST[0] = true;
        cut(0);
        // continue cut off and add new edge
        while (!pq.isEmpty()) {
            int[] edge = pq.poll();
            int to = edge[1];
            int weight = edge[2];
            if (inMST[to]) {
                // if node visited
                continue;
            }
            // append this edge
            weightSum += weight;
            inMST[to] = true;
            // cut new node
            cut(to);
        }
    }

    // cut node s
    private void cut(int s) {
        // traverse the adjacent edges
        for (int[] edge : graph[s]) {
            int to = edge[1];
            if (inMST[to]) {
                // if node visited
                continue;
            }
            // add this edge to pq
            pq.offer(edge);
        }
    }

    public int weightSum() {
        return weightSum;
    }

    // check if conver all nodes
    public boolean allConnected() {
        for (int i = 0; i < inMST.length; i++) {
            if (!inMST[i]) {
                return false;
            }
        }
        return true;
    }
}

```

## LeetCode
Kruskal
- 261.Graph Valid Tree (Kruskal)
- 1135.Connecting Cities With Minimum Cost (Kruskal \ Prim)
- 1584.Min Cost to Connect All Points (Kruskal \ Prim)

### 261. Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:

<img src="../../../static/261-1.jpeg">

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

Example 2:

<img src="../../../static/261-2.jpeg">

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.

#### Solution
We could use Union-Find to check if two connected nodes be union already.

```aidl
/*
 * Author @ LBLD
 * 12-19-2022
 */

class Solution {

    boolean validTree(int n, int[][] edges) {
        // initialize the union-find
        UF uf = new UF(n);
        // connect two nodes connected by one edge
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            // if these two nodes be union already
            if (uf.connected(u, v)) {
                return false;
            }
            // union these two nodes
            uf.union(u, v);
        }
        // check if only a single tree exists
        return uf.count() == 1;
    }

    class UF {
        private int count;
        private int[] parent;
        private int[] size;

        public UF(int n) {
            this.count = n;
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ)
                return;

            if (size[rootP] > size[rootQ]) {
                parent[rootQ] = rootP;
                size[rootP] += size[rootQ];
            } else {
                parent[rootP] = rootQ;
                size[rootQ] += size[rootP];
            }

            count--;
        }

        public boolean connected(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            return rootP == rootQ;
        }

        private int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public int count() {
            return count;
        }
    }
}
```

### 1135. Connecting Cities With Minimum Cost

There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.


Example 1:

<img src="../../../static/1135-1.png">

```
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
```

Example 2:

<img src="../../../static/1135-2.png">

```
Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
```

Constraints:
- 1 <= n <= 104
- 1 <= connections.length <= 104
- connections[i].length == 3
- 1 <= xi, yi <= n
- xi != yi
- 0 <= costi <= 105

#### Idea
We have known how to check and get a tree from graph using Union-Find. But how could we reach the minimum cost tree?

One idea is to sort the edge and start with the least weight edge, actually greedy algorithm.

#### Kruskal Solution
```aidl
/*
 * Author @ LBLD
 * 12-19-2022
 */
 
class Solution {
    int minimumCost(int n, int[][] connections) {
        // label start from 1
        UF uf = new UF(n + 1);
        // sort edge based on weight
        Arrays.sort(connections, (a, b) -> (a[2] - b[2]));
        // the minimum weight
        int mst = 0;
        // pick the minimum edge from sorted edge
        for (int[] edge : connections) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            // if cyclic edge
            if (uf.connected(u, v)) {
                continue;
            }
            
            mst += weight;
            uf.union(u, v);
        }
        // because node 0 won't be connected with tree
        // so check if count is euqal to 2
        return uf.count() == 2 ? mst : -1;
    }
    class UF {
        private int count;
        private int[] parent;
        private int[] size;

        public UF(int n) {
            this.count = n;
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ)
                return;

            if (size[rootP] > size[rootQ]) {
                parent[rootQ] = rootP;
                size[rootP] += size[rootQ];
            } else {
                parent[rootP] = rootQ;
                size[rootQ] += size[rootP];
            }
            count--;
        }

        public boolean connected(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            return rootP == rootQ;
        }

        private int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public int count() {
            return count;
        }
    }

}
```

#### Prim Solution
```aidl
/*
 * Author @ LBLD
 * 12-20-2022
 */
 
class Solution {
    public int minimumCost(int n, int[][] connections) {

        List<int[]>[] graph = buildGraph(n, connections);
        Prim prim = new Prim(graph);

        if (!prim.allConnected()) {
            return -1;
        }

        return prim.weightSum();
    }

    List<int[]>[] buildGraph(int n, int[][] connections) {
        List<int[]>[] graph = new LinkedList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] conn : connections) {
            int u = conn[0] - 1;
            int v = conn[1] - 1;
            int weight = conn[2];
            graph[u].add(new int[]{u, v, weight});
            graph[v].add(new int[]{v, u, weight});
        }
        return graph;
    }

    class Prim {
        private PriorityQueue<int[]> pq;
        private boolean[] inMST;
        private int weightSum = 0;
        private List<int[]>[] graph;

        public Prim(List<int[]>[] graph) {
            this.graph = graph;
            this.pq = new PriorityQueue<>((a, b) -> {
                return a[2] - b[2];
            });
            int n = graph.length;
            this.inMST = new boolean[n];

            inMST[0] = true;
            cut(0);
            while (!pq.isEmpty()) {
                int[] edge = pq.poll();
                int to = edge[1];
                int weight = edge[2];
                if (inMST[to]) {
                    continue;
                }
                weightSum += weight;
                inMST[to] = true;
                cut(to);
            }
        }

        private void cut(int s) {
            for (int[] edge : graph[s]) {
                int to = edge[1];
                if (inMST[to]) {
                    continue;
                }
                pq.offer(edge);
            }
        }

        public int weightSum() {
            return weightSum;
        }

        public boolean allConnected() {
            for (int i = 0; i < inMST.length; i++) {
                if (!inMST[i]) {
                    return false;
                }
            }
            return true;
        }
    }
}
```

### 1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the manhattan distance between them: `|xi - xj| + |yi - yj|`, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



Example 1:

<img src="../../../static/1584-1.png">

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
```
<img src="../../../static/1584-1.1.png">

```
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

Example 2:

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

Constraints:
- 1 <= points.length <= 1000
- -106 <= xi, yi <= 106
- All pairs (xi, yi) are distinct.

#### Idea
Generate all edges cost for each node pair, and then use Kruskal algorithm.

And we use the index rather than the coordinate (x, y), in this way we can use Union-Find algorithm in previous way.

#### Kruskal Solution
```aidl
/*
 * Author @ LBLD
 * 12-19-2022
 */
 
class Solution {
    int minCostConnectPoints(int[][] points) {
        int n = points.length;
        // calculate the distance for each two points
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xi = points[i][0], yi = points[i][1];
                int xj = points[j][0], yj = points[j][1];
                // edges: [index1, index2, distance]
                edges.add(new int[] {
                    i, j, Math.abs(xi - xj) + Math.abs(yi - yj)
                });
            }
        }
        // sort the edge based on distance
        Collections.sort(edges, (a, b) -> {
            return a[2] - b[2];
        });

        // Kruskal
        int mst = 0;
        UF uf = new UF(n);
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];

            if (uf.connected(u, v)) {
                continue;
            }

            mst += weight;
            uf.union(u, v);
        }
        return mst;
    }

    class UF {
        private int count;
        private int[] parent;
        private int[] size;

        public UF(int n) {
            this.count = n;
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ)
                return;

            if (size[rootP] > size[rootQ]) {
                parent[rootQ] = rootP;
                size[rootP] += size[rootQ];
            } else {
                parent[rootP] = rootQ;
                size[rootQ] += size[rootP];
            }
            count--;
        }

        public boolean connected(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            return rootP == rootQ;
        }

        private int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public int count() {
            return count;
        }
    }
}
```

#### Prim Solution
```aidl
/*
 * Author @ LBLD
 * 12-20-2022
 */

class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        List<int[]>[] graph = buildGraph(n, points);
        return new Prim(graph).weightSum();
    }

    List<int[]>[] buildGraph(int n, int[][] points) {
        List<int[]>[] graph = new LinkedList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xi = points[i][0], yi = points[i][1];
                int xj = points[j][0], yj = points[j][1];
                int weight = Math.abs(xi - xj) + Math.abs(yi - yj);
                graph[i].add(new int[]{i, j, weight});
                graph[j].add(new int[]{j, i, weight});
            }
        }
        return graph;
    }

    class Prim {
        private PriorityQueue<int[]> pq;
        private boolean[] inMST;
        private int weightSum = 0;
        private List<int[]>[] graph;

        public Prim(List<int[]>[] graph) {
            this.graph = graph;
            this.pq = new PriorityQueue<>((a, b) -> {
                return a[2] - b[2];
            });
            int n = graph.length;
            this.inMST = new boolean[n];

            inMST[0] = true;
            cut(0);
            while (!pq.isEmpty()) {
                int[] edge = pq.poll();
                int to = edge[1];
                int weight = edge[2];
                if (inMST[to]) {
                    continue;
                }
                weightSum += weight;
                inMST[to] = true;
                cut(to);
            }
        }

        private void cut(int s) {
            for (int[] edge : graph[s]) {
                int to = edge[1];
                if (inMST[to]) {
                    continue;
                }
                pq.offer(edge);
            }
        }

        public int weightSum() {
            return weightSum;
        }

        public boolean allConnected() {
            for (int i = 0; i < inMST.length; i++) {
                if (!inMST[i]) {
                    return false;
                }
            }
            return true;
        }
    }
}
```

#### Kruskal Complexity
Space Complexity: O(V + E)

Because we need all of the edges E to sort, and Union-Find need all of the nodes V.

Time Complexity: O(ElogE)

Because sort will cost O(ElogE), for loop cost O(E).

#### Prim Complexity
Time Complexity: O(ElogE)

Because we need to add E edges, so it is O(logE), and then we will go over all edges.