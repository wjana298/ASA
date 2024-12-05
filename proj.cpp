#include <iostream>
#include <vector>
#include <string>

using namespace std;

void setOperations(int n, vector<vector<int>> *operations) {
    for (int i = 0; i < n; ++i) {                           // reading the matrix
        for (int j = 0; j < n; ++j) {                       // quando o projeto estiver pronto, mudar para argv
            cin >> (*operations)[i][j];
        }
    }
}

void setSequence(int m, vector<int> *sequence) {
    for (int i = 0; i < m; i++){                             // reading the sequence
        cin >> (*sequence)[i];
    }
}

int main(int argc, char *argv[]) {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    // Usei cin, porque é mais simples de visualizar, mas acho que argv seria melhor
    // n = size of the matrix, m = size of the sequence, r = result
    int n, m;
    int r;
    cin >> n >> m;

    /* iniciar a matrix com os resultados das operações*/
    vector<vector<int>> operations(n, vector<int>(n));      // matrix of size n x n with operations
    setOperations(n, &operations);

    /* iniciar o vetor com a sequência a resolver */
    vector<int> sequence(m);
    setSequence(m, &sequence);

    /* valor a encontrar */
    cin >> r;

    /* matrix para resolver o problema */
    vector<vector<vector<int>>> matrizDeResultados(m, vector<vector<int>>(m));  // m x m x k, em que k são as posições dos parenteses
    
    for (int i = 0; i < m; i++) {
        matrizDeResultados[i][i].push_back(sequence[i]);    // casos base
    }

    for (int start = 0; )

    return 0;
}