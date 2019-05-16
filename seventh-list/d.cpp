#include <iostream>
#include <algorithm>

using namespace std;

struct edge {
    int x, y, z;
};

bool comp(edge a, edge b) { 
    return a.z < b.z; 
}

// union find
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


int main(){
  
  while(true) {
  
    int nVertices, nArestas; // número de vértices e arestas
  
    cin >> nVertices >> nArestas;
    
    if(nArestas == 0 && nVertices == 0) {
      break;
    }
    
    edge mst[nVertices-1];
    edge edges[nArestas];
    
    for(int i = 0; i < nArestas; ++i) {
        cin >> edges[i].x >> edges[i].y >> edges[i].z;
    }
    
    int parent[nVertices];
    
    // inicializar os pais para o union-find (make-set)
    for(int i = 0; i < nVertices; ++i) {
        parent[i] = -1;
    }
    
    int total_cost = 0;
    
    // ordenar as arestas
    sort(edges, edges + nArestas, comp);
    
    
    int mst_size = 0;
    //for each edge, verify if vertices are in the same set
    for(int i = 0; i < nArestas; ++i) {
        int a = find(parent, edges[i].x);
        int b = find(parent, edges[i].y);
        total_cost += edges[i].z;
        
        if(a != b) {
            mst[mst_size++] = edges[i];
            join(parent, a, b);
        }
    }
    
    int best_cost = 0;
    
    for(int i = 0; i < nVertices-1; i++) {
        best_cost += mst[i].z;
    }
    
    cout << total_cost - best_cost << endl;
    
  }
    
    return 0;
}