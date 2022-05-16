#include "foo.h"

/**
 * @brief Sums two integer numbers.
 *
 * @param x First number.
 * @param y Second number.
 * @return int Sum of x and y.
 */
int summing(int x, int y) {
    return x + y;
}

/**
 * @brief Sums the vector y into x.
 * 
 * @param x Accumulator vector.
 * @param y Vector summed to x.
 * @param len length of the vector.
 */
int* sum_vectors(int* x, int* y, int len) {
    for (int i = 0; i < len; i++) {
        x[i] += y[i];
    }
}

/**
 * @brief Summs two complex numbers.
 * 
 * @param x First complex number.
 * @param y Second complex number.
 * @return struct cpx Sum of x and y.
 */
struct cpx sum_cpx(struct cpx x, struct cpx y) {
    struct cpx z;
    z.r = x.r + y.r;
    z.i = x.i + y.i;
    return z;
}