#include <stdio.h>

int func (void)
{
    return 1;
}

//int (*test) (void) = func;

int main (void)
{
    int (*test) (void);
    test = func;
    
    printf("%i \n", test());
    
    return 0;
}