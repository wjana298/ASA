#include <iostream>
#include <vector>
#include <string>

using namespace std;


// Função para ler a matriz de operações
void setOperations(int n, vector<vector<int>> *operations) {
    for (int i = 0; i < n; ++i) {                           // reading the matrix
        for (int j = 0; j < n; ++j) {                       // quando o projeto estiver pronto, mudar para argv
            cin >> (*operations)[i][j];
        }
    }
}

// Função para ler a sequência
void setSequence(int m, vector<int> *sequence) {
    for (int i = 0; i < m; i++){                             // reading the sequence
        cin >> (*sequence)[i];
    }
}

// Função para fazer operações entre listas de valores
void operation(vector<int> a, vector<int> b, vector<vector<int>> *operations) {
    for (size_t i = 0; i < a.size(); i++) {
        for (size_t j = 0; j < b.size(); j++) {
            cout << a[i] << " " << b[j] << " " << (*operations)[a[i]][b[j]] << endl;
        }
    }
}

vector<pair<int, int>> calculatePossibleResults(int i, int j, 
                                                vector<vector<int>> *operations, vector<int> *sequence, 
                                                vector<vector<vector<pair<int, int>>>> *matrizDeResultados) {
	vector<pair<int, int>> possibleResults;

    if (i == j) {
        possibleResults.push_back({{(*sequence)[i]}, -1});
        return possibleResults;
    }

    for (int k = j -1; k >= i; k--) {
        operation((*matrizDeResultados)[i][k], (*matrizDeResultados)[k+1][j], operations);
    }

	return possibleResults;
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    // Usei cin, porque é mais simples de visualizar, mas acho que argv seria melhor
    // n = size of the matrix, m = size of the sequence, r = result
    int n, m;
    int r;
    cin >> n >> m;

    /* iniciar a matrix com os resultados das operações*/
    vector<vector<int>> operacoes(n, vector<int>(n));      // matrix of size n x n with operations
    setOperations(n, &operacoes);

    /* iniciar o vetor com a sequência a resolver */
    vector<int> sequencia(m);
    setSequence(m, &sequencia);

    /* valor a encontrar */
    cin >> r;

    /* matrix para resolver o problema */
    vector<vector<vector<pair<int, int>>>> matrizDeResultados(m, vector<vector<pair<int, int>>>(m));  // m x m x k, em que k são as posições dos parenteses

    for (int start = 0; start < m; start++) {
        int i = 0, j = start;               // j = coluna, i = linha

        while (i < m) {                     // isto vai iterar sobre a matriz diagonalmente
			cout << i << " " << j << "\t";
            matrizDeResultados[i][j] = calculatePossibleResults(i, j, &operacoes, &sequencia, &matrizDeResultados);
            j++;
			i++;
        }
		cout << endl;
    }

    return 0;
}