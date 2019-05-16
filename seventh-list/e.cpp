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
    
    int nVertices, nArestas, nFerrovias, nEstradas;// número de vértices e arestas

    cin >> nVertices >> nFerrovias >> nEstradas;
    nArestas = nFerrovias + nEstradas;

    edge mst[nVertices-1];
    edge edges[nArestas];
    edge ferrovias[nFerrovias];
    edge estradas[nEstradas];

    for(int i = 0; i < nFerrovias; ++i) {
        cin >> ferrovias[i].x >> ferrovias[i].y >> ferrovias[i].z;
        ferrovias[i].x--;
        ferrovias[i].y--;
    }
    for(int i = 0; i < nEstradas; ++i) {
        cin >> estradas[i].x >> estradas[i].y >> estradas[i].z;
        estradas[i].x--;
        estradas[i].y--;
    }

    int parent[nVertices];

    // inicializar os pais para o union-find (make-set)
    for(int i = 0; i < nVertices; ++i) {
        parent[i] = -1;
    }

    int total_cost = 0;

    // ordenar as arestas
    sort(ferrovias, ferrovias + nFerrovias, comp);
    sort(estradas, estradas + nEstradas, comp);
    for(int i = 0; i < nFerrovias; i++) {
        edges[i] = ferrovias[i];
    }
    for(int i = 0; i < nEstradas; i++) {
        edges[i + nFerrovias] = estradas[i]; 
    }

    int mst_size = 0;
    //for each edge, verify if vertices are in the same set
    for(int i = 0; i < nArestas; ++i) {
        int a = find(parent, edges[i].x);
        int b = find(parent, edges[i].y);
        total_cost += edges[i].z;

        if(a != b && edges[i].z) {
            mst[mst_size++] = edges[i];
            join(parent, a, b);
        }
    }

    int best_cost = 0;

    for(int i = 0; i < nVertices-1; i++) {
        best_cost += mst[i].z;
    }

    cout << best_cost << endl;
}