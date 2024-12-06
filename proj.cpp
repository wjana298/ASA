#include <iostream>
#include <vector>
#include <string>
#include <tuple>

using namespace std;

// vector<tuple<int, int, int, int>> calculatePossibleResults(int i, int j, 
//                                                 vector<vector<int>> *operations, vector<int> *sequence, 
//                                                 vector<vector<vector<tuple<int, int, int, int>>>> *matrizDeResultados) {
// 	vector<tuple<int, int, int, int>> possibleResults;

//     if (i == j) {
//         possibleResults.push_back(make_tuple((*sequence)[i], -1, -1, -1));
//         cout << "i == j == " << (*sequence)[i] << endl;
//         return possibleResults;
//     }

//     vector<tuple<int, int, int, int>> primeiro, segundo;

//     for (int k = j - 1; k >= i; k--) {
//         primeiro = (*matrizDeResultados)[i][k];
//         segundo = (*matrizDeResultados)[k+1][j];

//         for(int a = 0; a < primeiro.size(); a++){
//             for(int b = 0; b < segundo.size; b++){
                
//             }
//         }
        
//     }
// 	return possibleResults;


//     M[1][3] = M[1][1] + M[2][3], M[1][2] + M[3][3].

//     M[1][1] -> 2 tuple<2, 1, -1, -1>
//     M[2][3] -> 3 tuple<3, 1, -1, -1>
//     possibleResults = operations[primeiro[0][0], segundo[0][0]];

//     primeiro = M[1][2] -> {1,2,3} tuple<1, 2, -1, -1>, tuple<2,3,-1,-1>, tuple<3,3,-1,-1>
//     segundo = M[3][3] -> {1,2} tuple<1, 1, -1, -1>, tuple<2, 2, -1, -1>

//     for(primeiro[a] : m)
//         for(segundo[b] : m)
//             possibleResults = operations[primeiro[a][0] + segundo [b][0]];



// }

vector<tuple<int, int, int, int>> calculatePossibleResults(
    int i, int j, 
    vector<vector<int>> *operations, 
    vector<int> *sequence, 
    vector<vector<vector<tuple<int, int, int, int>>>> *matrizDeResultados) {
    
    vector<tuple<int, int, int, int>> possibleResults;

    // Caso base: i == j, retorna o valor diretamente da sequência
    if (i == j) {
        possibleResults.push_back(make_tuple((*sequence)[i], -1, -1, -1));
        cout << "i == j == " << (*sequence)[i] << endl;
        return possibleResults;
    }

    // Combinar os subproblemas
    for (int k = i; k <= j; k++) {  // Dividir a sequência em (i..k) e (k+1..j)
        const auto &leftResults = (*matrizDeResultados)[i][k];
        const auto &rightResults = (*matrizDeResultados)[k + 1][j];

        for (const auto &left : leftResults) {
            for (const auto &right : rightResults) {
                // Obter os valores das subpartes
                int leftValue = get<0>(left);
                int rightValue = get<0>(right);

                // Realizar a operação binária
                int result = (*operations)[leftValue - 1][rightValue - 1];

                // Adicionar o resultado e o índice de divisão k
                possibleResults.push_back(make_tuple(result, i, j, k));
                cout << result << " " << i+1 << " " << j+1 << " " << k+1 << endl;
            }
        }
    }

    return possibleResults;
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    // Usei cin, porque é mais simples de visualizar, mas acho que argv seria melhor
    // n = size of the matrix, m = size of the sequence, r = result
    int n, m;
    cin >> n >> m;

    /* iniciar a matrix com os resultados das operações*/
    vector<vector<int>> operacoes(n, vector<int>(n));      // matrix of size n x n with operations
    for (int i = 0; i < n; ++i) {                           // reading the matrix
        for (int j = 0; j < n; ++j) {                       // quando o projeto estiver pronto, mudar para argv
            cin >> operacoes[i][j];
        }
    }

    /* iniciar o vetor com a sequência a resolver */
    vector<int> sequencia(m);
        for (int i = 0; i < m; i++){                    // reading the sequence
        cin >> sequencia[i];
    }

    /* valor a encontrar */
    int r;
    cin >> r;

    /* matrix para resolver o problema */
    vector<vector<vector<tuple<int, int, int, int>>>> matrizDeResultados (m, vector<vector<tuple<int, int, int, int>>>(m));  // m x m x k, em que k são as posições dos parenteses

    for (int start = 0; start < m; start++) {
        int i = 0, j = start;               // j = coluna, i = linha

        while (j < m) {                     // isto vai iterar sobre a matriz diagonalmente
			cout << i+1 << " " << j+1 << "\n";
            matrizDeResultados[i][j] = calculatePossibleResults(i, j, &operacoes, &sequencia, &matrizDeResultados);
            j++;
			i++;
        }
		cout << endl;
    }

    return 0;
}