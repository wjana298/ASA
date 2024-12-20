/**
 * @file project.cpp
 * @brief Implementação do segundo projeto de ASA.
 *
 * O projeto usa duas listas, uma com as estações que pertecem a cada linha e outra
 * com as linhas que passam por cada estação. A partir destas duas listas, criamos um
 * grafo de linhas para linhas, onde cada nó é uma linha e as arestas são as ligações
 * entre as linhas. De seguida podemos fazer uma BFS para encontrar o maior indice
 * de conectividade.
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

/*  Grafo Linha - Linha */
vector<set<int>> graph;
/*  Lista de linhas que passam por cada estação */
vector<set<int>> node_line_graph;   
/*  Lista de estações que pertencem a cada linha */
vector<set<int>> line_node_graph;

/**
 * @brief Função que remove linhas repetidas
 * 
 * Percorre todas as linhas e verifica se estão contidas noutra linha.
 * Se estiverem, o algoritmo remove a linha que está contida.
 */
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

/**
 * @brief Função que faz uma BFS para encontrar o maior indice de conectividade
 * 
 * @param start - linha de inicio
 * @return int - maior indice de conectividade
 */
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

    // se uma estação não pertencer a nenhuma linha, devolve -1 e termina
    for(auto &i : node_line_graph) {
        if(i.empty()) {
            cout << -1 << endl;
            return 0;
        }
    }

    // Remover linhas repetidas
    remover_repetidos();

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

    // Encontrar o maior indice de conectividade a partir do grafo linhas-linhas
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