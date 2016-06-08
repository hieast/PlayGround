#include <stdio.h>

int int_size (void)
{
    unsigned int i = ~0;
    int result = 0;
    for (;i != 0; i>>=1)
        result++;
    return result;
}

int main (void)
{
    printf ("%i\n", int_size());
    
    return 0;
}