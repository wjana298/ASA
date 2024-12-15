/* Projeto 1 de ASA 
TP040, Joana Guia 99147, Miguel Trêpa 109370
*/

#include <iostream>
#include <vector>
#include <string>
#include <tuple>

using namespace std;

string obter_parentizacao(int i, int j, int resultado_esperado,
                                 vector<vector<vector<tuple<int, int, int, int>>>> &matriz_de_resultados,
                                 vector<vector<string>> &tabela_de_parenteses) {
    if (tabela_de_parenteses[i][j] != "") return tabela_de_parenteses[i][j];        // Se já existir a parentização, devolve-a

    if (i == j) {                                                                           
        tabela_de_parenteses[i][j] = to_string(get<0>(matriz_de_resultados[i][j][0]));  // No caso de m = 1, devolve sequencia[0]
        return tabela_de_parenteses[i][j];
    }

    for (const auto &res : matriz_de_resultados[i][j]) {                            // Percorre os resultados possíveis
        int valor = get<0>(res);
        int k = get<1>(res);
        int esq = get<2>(res);
        int dir = get<3>(res);
        
        if (valor == resultado_esperado) {                                          
            // Obter a parentização já calculada para a esquerda e para a direita
            string parcela_esquerda = obter_parentizacao(i, k, esq, matriz_de_resultados, tabela_de_parenteses);
            string parcela_direita = obter_parentizacao(k + 1, j, dir, matriz_de_resultados, tabela_de_parenteses);

            tabela_de_parenteses[i][j] = "(" + parcela_esquerda + " " + parcela_direita + ")";  // Coloca os parenteses no problema atual
            return tabela_de_parenteses[i][j];
        }
    }

    return "";
}

vector<tuple<int, int, int, int>> calcular_resultados_possiveis(int i, int j, int n,
                                                vector<vector<int>> *operacoes, vector<int> *sequencia, 
                                                vector<vector<vector<tuple<int, int, int, int>>>> *matriz_de_resultados) {

	vector<tuple<int, int, int, int>> resultados_possiveis;     // {valor, k, valor da esquerda usado na sua operacao, valor da direita "}

    //Preenche diagonal principal com v=i e k=-1
    if (i == j) {
        resultados_possiveis.push_back(make_tuple((*sequencia)[i], -1, -1, -1));
        return resultados_possiveis;
    }

    //Vetor auxiliar para saber se já obtivemos todos os valores possiveis de n
    vector<int> seq(n,-1);
    
    //Loop que percorre todas opcoes de k na célula [i,j]
    // M[i,j] = M[i,k] + M[k+1,j] para i <= k < j
    for (int k = j - 1; k >= i; k--) {
        const auto &parcela_esquerda = (*matriz_de_resultados)[i][k];
        const auto &parcela_direita = (*matriz_de_resultados)[k+1][j];
        for (const auto &esq : parcela_esquerda){
            for (const auto &dir : parcela_direita){
                int valor_esq = get<0>(esq);
                int valor_dir = get<0>(dir);

                int resultado = (*operacoes)[valor_esq - 1][valor_dir - 1];

                // Verifica se este n já foi encontrado. Se não tiver sido então guarda-o com o k e valores respetivos.
                if(resultado != seq[resultado - 1]){
                    seq[resultado-1] = resultado;
                    resultados_possiveis.push_back(make_tuple(resultado, k, valor_esq, valor_dir));
                }

                // Se resultados_possiveis tiver o mesmo tamanho que n, significa que encontramos todos os valores possiveis de n
                if (resultados_possiveis.size() == static_cast<size_t>(n)) {
                    return resultados_possiveis;
                }
            }
        }
    }

	return resultados_possiveis;
}


int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);                    

    // Obter tamanho da matriz de operações e da sequência
    int n, m;
    cin >> n >> m;

    // Obter a matriz de operações |n x n|
    vector<vector<int>> operacoes(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> operacoes[i][j];
        }
    }

    // Obter a sequência a resolver |m|
    vector<int> sequencia(m);
        for (int i = 0; i < m; i++){
        cin >> sequencia[i];
    }

    // Resultado esperado
    int r;
    cin >> r;
    
    // Matriz de resultados
    vector<vector<vector<tuple<int, int, int, int>>>> matriz_de_resultados (m, vector<vector<tuple<int, int, int, int>>>(m));

    // Preencher a matriz de resultados diagonalmente, começando na diagonal i == j até ao canto superior direito
    for (int len = 1; len <= m; ++len) {
        for (int i = 0; i + len - 1 < m; ++i) {
            int j = i + len - 1;
            matriz_de_resultados[i][j] = calcular_resultados_possiveis(i, j, n, &operacoes, &sequencia, &matriz_de_resultados);
        }
    }

    // Verifica se o resultado esperado é possível
    bool existe = false;
    for (const auto &res : matriz_de_resultados[0][m - 1]) {        
        if (get<0>(res) == r) {
            existe = true;
            break;
        }
    }

    // Gerar o output
    if (existe) {
        cout << "1\n";                                     
        vector<vector<string>> tabela_de_parenteses(m, vector<string>(m, ""));                  // Tabela de parentizações para memoização
        cout << obter_parentizacao(0, m - 1, r, matriz_de_resultados, tabela_de_parenteses) << endl;
    } else {
        cout << "0\n";                                                                          // Se não existe solução
    }

    return 0;
}