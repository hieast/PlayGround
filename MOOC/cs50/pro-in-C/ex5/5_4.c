#include <stdio.h>

int main(void)
{
    int n, factor;

    printf ("TABLE OF FACTOR NUMBERS\n\n");
    printf ("n      product from 1 to n\n");
    printf ("---------------------------\n");
    
    factor = 1;  
    
    for (n = 1; n < 11; n++)
    {
        factor *= n;
        printf ("%-2i           %i\n", n, factor);
    }
    return 0;
}