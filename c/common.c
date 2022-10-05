#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "common.h"

void reset(struct Grid * grid) {
    memset(grid->grid, 0, sizeof(grid->grid));
    new_tile(grid);
    new_tile(grid);
}

void rotate_90(struct Grid * grid) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3-2*i; j++) {
            long tmp = grid->grid[i][i+j];
            grid->grid[i][i+j] = grid->grid[3-i-j][i];
            grid->grid[3-i-j][i] = grid->grid[3-i][3-i-j];
            grid->grid[3-i][3-i-j] = grid->grid[i+j][3-i];
            grid->grid[i+j][3-i] = tmp;
        }
    }
}

void rotate(struct Grid * grid, int n) {
    for (int i = 0; i<n; i++) {
        rotate_90(grid);
    }
}

void new_tile(struct Grid * grid) {
    //count empty tiles
    int num_empty = 0;
    for (int x=0; x<4; x++) {
        for (int y=0; y<4; y++) {
            if (grid->grid[x][y] == 0) num_empty++;
        }
    }
    // get random empty tile
    int tile_index = rand() % num_empty;
    int checked_tiles = 0;
    for (int x=0; x<4; x++) {
        for (int y=0; y<4; y++) {
            // for every empty tile
            if (grid->grid[x][y] == 0) {
                // check if its the one chosen eariler
                if (checked_tiles == tile_index) {
                    //generate new tile here
                    long new_val = 2;
                    if ((float)rand()/(float)(RAND_MAX) > 0.8) {
                        new_val = 4;
                    }
                    grid->grid[x][y] = new_val;
                    // quit function
                    return;
                }
                // else, "mark as checked"
                checked_tiles++;
            }
        }
    }
}

bool gameover(struct Grid *  grid) {
    //available emtpy tiles
    for (int x=0; x<4; x++) {
        for (int y=0; y<4; y++) {
            if (grid->grid[x][y] == 0) {
                return false;
            }
        }
    }
    //availablle veritcal merges
    for (int y=0; y<3; y++) {
        for (int x; x<4; x++) {
            if (grid->grid[x][y] == grid->grid[x][y+1]) {
                return false;
            }
        }
    }
    //available horizontal merges
    for (int y=0; y<4; y++) {
        for (int x=0; x<3; x++) {
            if (grid->grid[x][y] == grid->grid[x+1][y]) {
                return false;
            }
        }
    }
    return true;
}
