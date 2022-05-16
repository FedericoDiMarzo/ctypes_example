#pragma once

/**
 * @brief Structure that holds complex numbers
 */
struct cpx
{
    float r, i;
};


int summing(int x, int y);

int* sum_vectors(int* x, int* y, int len);

struct cpx sum_cpx(struct cpx x, struct cpx y);

