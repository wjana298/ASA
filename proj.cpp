#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
 *  calculateSolution: function to calculate the solution of the problem using dynamic programming 
 * 
 *  INPUT:
 *      n: size of the matrix
 *      m: size of the sequence
 *      operations: matrix of size n x n with operations
 *      sequence: vector with the sequence to solve
 *      solutions: matrix for calculation of the final solution
 * 
 *  OUTPUT:
 *      completed solutions matrix
 * */
void calculateSolution(int n, int m,
                        vector<vector<int>> *operations,
                        vector<int> *sequence,
                        vector<vector<vector<pair<int, int>>>> *solutions) {
    
    cout << "calculateSolution: started" << endl;

    cout << "calculateSolution: ended" << endl;
    }

void initializeSolution(int m,
                        vector<int> *sequence,
                        vector<vector<vector<pair<int, int>>>> *solutions) {
    
    cout << "initializeSolution: started" << endl;

    for (int i = 0; i < m; i++) {
        (*solutions)[i][i].push_back(make_pair((*sequence)[i], 0));
        cout << (*solutions)[i][i][0].first << " " << (*solutions)[i][i][0].second << endl;
        }

    cout << "initializeSolution: ended" << endl;
    }

int main(int argc, char *argv[]) {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    // Usei cin, porque é mais simples de visualizar, mas acho que argv seria melhor
    // n = size of the matrix, m = size of the sequence, r = result
    int n, m;
    int r;
    cin >> n;                   
    cin >> m;
    cout << n << " " << m << endl;

    vector<vector<int>> operations(n, vector<int>(n));      // matrix of size n x n with operations
    for (int i = 0; i < n; ++i) {                           // reading the matrix
        for (int j = 0; j < n; ++j) {
            cin >> operations[i][j];
            cout << operations[i][j] << " ";
        }
        cout << endl;
    }

    vector<int> sequence(m);
    for (int i = 0; i < m; i++){                             // reading the sequence
        cin >> sequence[i];
        cout << sequence[i] << " ";
    }
    cout << endl;

    cin >> r;
    cout << r << endl;

    vector<vector<vector<pair<int, int>>>> solutions(m, vector<vector<pair<int, int>>>(m));      // matrix for calculation of the final solution

    initializeSolution(m, &sequence, &solutions);
    
    for (int start = 1; start < m; start++) {               // percorre a matriz de soluções apenas nas casas relevantes
        int i = start, j = 0;
    }

    return 0;
}