/**
 * @file project.cpp
 * @brief This file contains the implementation of the second project for ASA.
 *
 * Meter aqui uma descrição do projeto assim que percebermos o que é suposto fazer. 
 * 
 * 
 *
 * @author Miguel Trêpa (109370) & Joana Guia (99147)
 * @date 15-12-2020
 */

#include <iostream>

int main() {
    int V, E, L;
    
    int n = scanf("%d %d %d", &V, &E, &L);
    if(n != 3) {
        printf("ERROR: Wrong number of arguments\n");
        return 1;
    }

    printf("V: %d, E: %d, L: %d\n", V, E, L);

    V += E + L;
    return 0;
}