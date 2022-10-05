#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#include "common.h"

int main() {
    struct Grid test;
    test.score = 0;
    memset(test.grid, 0, sizeof(test.grid));

    test.grid[0][0] = 1;
    test.grid[1][1] = 2;
    test.grid[2][2] = 3;
    test.grid[3][3] = 4;

    for (int i=0; i < 4; i++) {
        printf("|");
        for (int j=0; j < 4; j++) {
            printf(" %li |", test.grid[i][j]);
        }
        printf("\n");
    }

    rotate_90(&test);

    printf("\n");

    for (int i=0; i < 4; i++) {
        printf("|");
        for (int j=0; j < 4; j++) {
            printf(" %li |", test.grid[i][j]);
        }
        printf("\n");
    }
}
