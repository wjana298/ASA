/**
 * @file project.cpp
 * @brief This file contains the implementation of the second project for ASA.
 *
 * Meter aqui uma descricao do projeto assim que percebermos o que e suposto fazer. 
 * 
 * 
 *
 * @author Miguel Trepa (109370) & Joana Guia (99147)
 * @date 15-12-2020
 */

#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int stations, connections , lines;
int lines_removed = 0;

/*  Gráfo com apenas as linhas */
vector<set<int>> graph;
/*  Lista de linhas que passam por cada estação */
vector<set<int>> node_line_graph;   
vector<set<int>> line_node_graph;


void remover_repetidos (){
    for (int i = 0; i < lines; i++) {
        auto& ui = line_node_graph[i];
        if (ui.empty()) continue;
        
        for(int j = 0; j < lines; j++){
            if (i==j) continue;
            auto& oi = line_node_graph[j];
            if(oi.empty()) continue;
            if(includes(oi.begin(), oi.end(), ui.begin(), ui.end())) {
                // Clear line from nodes
                for(int node : ui) {
                    node_line_graph[node].erase(i);
                } 
                ui.clear();
                lines_removed++;
            }
        }
    }
}

int BFS(int start){
    vector<bool> visited(lines, false);
    queue<pair<int,int>> q;
    int total_changes = 0;
    int total_lines = lines;

    visited[start] = true;
    q.emplace(start, 0); // pair(line, changes)

    while (!q.empty()) {
        if(total_lines == 0) {
            break;
        }
        pair<int,int> current = q.front();
        int line = current.first;
        int changes = current.second;
        q.pop();

        total_changes = changes;
        total_lines--;

        for (int neighbor : graph[line]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.emplace(neighbor, changes + 1);
            }
        }
    }

    if(total_lines - lines_removed != 0) {
        return -1;
    }
    return total_changes;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> stations >> connections >> lines;

    // Vetor para representar quais as linhas que passam por uma estação
    node_line_graph = vector<set<int>>(stations, set<int>());
    line_node_graph = vector<set<int>>(lines, set<int>());

    for (int i = 0; i < connections; i++) {
        int  x, y, l;

        // Processar o input
        cin >> x >> y >> l;
        x = x - 1;  // Para começar em 0
        y = y - 1;
        l = l - 1;

        // Adicionar a linha as estaçoes
        node_line_graph[x].insert(l);
        node_line_graph[y].insert(l);
        // Adicionar as estaçoes a linha
        line_node_graph[l].insert(x);
        line_node_graph[l].insert(y);
    }

    for(auto &i : node_line_graph) {
        if(i.empty()) {
            cout << -1 << endl;
            return 0;
        }
    }

    // // print node_line_graph
    // for(int i = 0; i < stations; i++) {
    //     cout << i+1 << ": ";
    //     for(int j : node_line_graph[i]) {
    //         cout << j+1 << " ";
    //     }
    //     cout << endl;
    // }

    // // print line_node_graph
    // for(int i = 0; i < lines; i++) {
    //     cout << i+1 << ": ";
    //     for(int j : line_node_graph[i]) {
    //         cout << j+1 << " ";
    //     }
    //     cout << endl;
    // }

    // Remover linhas repetidas
    remover_repetidos();

    // for(int i = 0; i < lines; i++) {
    //     cout << i+1 << ": ";
    //     for(int j : line_node_graph[i]) {
    //         cout << j+1 << " ";
    //     }
    //     cout << endl;
    // }

    // // print node_line_graph
    // for(int i = 0; i < stations; i++) {
    //     cout << i+1 << ": ";
    //     for(int j : node_line_graph[i]) {
    //         cout << j+1 << " ";
    //     }
    //     cout << endl;
    // }

    // Criar grafo final de linhas-linhas
    graph = vector<set<int>>(lines, set<int>());
    for(int line = 0; line < lines; line++) {
        if(line_node_graph[line].empty()) {
            continue;
        }
        for(int node : line_node_graph[line]) {
            for(int l : node_line_graph[node]) {
                if(l != line) {
                    graph[line].insert(l);
                }
            }
        }
    }

    int connectivity = 0;
    for(int i = 0; i < lines; i++) {
        int tmp = BFS(i);
        if(tmp == -1) {
            connectivity = -1;
            break;
        };
        connectivity = max(connectivity, tmp);
    }

    cout << connectivity << endl;

    return 0;
}