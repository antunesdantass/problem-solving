#include <iostream>
#include <algorithm>
#include <list>
#include <vector>

using namespace std;

struct edge {
    int x, y, z;
};

bool comp(edge a, edge b) { 
    return a.z < b.z; 
}

int find(int parent[], int v) {
    if (parent[v] == -1)
      return v;
    return find(parent, parent[v]);
}

void join(int parent[], int x, int y) {
    int xset = find(parent, x);
    int yset = find(parent, y);
    parent[xset] = yset;
}

int maxTrip(vector<edge> adj[], int x, int V) {
    bool *visited = new bool[V];
    int distance[V];
    for(int i = 0; i < V; i++) {
        visited[i] = false;
        distance[i] = INT_MAX;
    }

    list<int> queue;
    visited[x] = true;
    distance[x] = 0;
    queue.push_back(x);
    int maxDis = 0;
    while(!queue.empty()) {
        x = queue.front();
        queue.pop_front();
        for(int i = 0; i < adj[x].size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                distance[adj[x][i].x] = distance[x] + 1;
                maxDis = distance[x] + 1 > maxDis ? distance[x] + 1 : maxDis;
                queue.push_back(i);
            }
        }
    }

    return maxDis;
}

int main(){
    
    int nVertices, nArestas;

    cin >> nVertices >> nArestas;

    edge mst[nVertices-1];
    edge edges[nArestas];

    for(int i = 0; i < nArestas; ++i) {
        cin >> edges[i].x >> edges[i].y >> edges[i].z;
    }

    int parent[nVertices];

    for(int i = 0; i < nVertices; ++i) {
        parent[i] = -1;
    }

    int total_cost = 0;

    sort(edges, edges + nArestas, comp);

    int mst_size = 0;
    int maxCost = 0;

    for(int i = 0; i < nArestas; ++i) {
        int a = find(parent, edges[i].x);
        int b = find(parent, edges[i].y);
        total_cost += edges[i].z;

        if(a != b) {
            mst[mst_size++] = edges[i];
            join(parent, a, b);
        }
    }
    vector<edge> adj[nVertices - 1];
    for (int i = 0; i < nVertices - 1; i++) {
        edge v = mst[i];
        adj[v.x].push_back(v);
    }
    int maxDis = INT_MAX;
    for (int i = 0; i < nVertices - 1; i++) {
        int dis = maxTrip(adj, i, nVertices - 1);
        maxDis = dis < maxDis ? dis : maxDis;
    }

    cout << maxDis << endl;
}