#include <stdio.h>

static int i = 5;

int main (void)
{
    printf ("%i ", i);
    foo();
    
    printf ("%i \n", i);
    return 0;
}