#include <stdio.h>

#define MIN(x, y) ((x)<(y)?(x):(y))
#define MAX(x, y) ((x)>(y)?(x):(y))
#define MAX3(x, y, z) MAX(MAX(x, y), z)
#define SHIFT

int main(void)
{
    int a = 1, b = 2, c = 3;
    printf("min = %i\n", MIN(a, b));
    printf ("max3 = %i\n", MAX3(a, b, c));
    
    return 0;
}