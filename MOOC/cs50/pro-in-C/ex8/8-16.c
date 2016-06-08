#include <stdio.h>

unsigned long int factorial (unsigned int n)
{
    if (n == 0)
        return 1;
    else
        return n * factorial (n - 1);
}

int main (void)
{
    unsigned int j;

    for ( j = 0; j < 11; ++j )
        printf ("%2u! = %lu\n", j, factorial (j));
    return 0;
}