#ifndef COMMON_H
#define COMMON_H

struct Grid{
    long grid[4][4];
    long score;
};
void rotate_90(struct Grid * grid);
void rotate(struct Grid * grid, int n);
void new_tile(struct Grid * grid);
void reset(struct Grid * grid);
bool gameover(struct Grid *  grid);

#endif
