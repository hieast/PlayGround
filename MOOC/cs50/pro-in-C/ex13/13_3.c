#include <stdio.h>

#define ABSOLUTE_VALUE(x) (((x) > 0) ? x : -x)

int main (void)
{
    int a = -1, b = 0, c = 1;
    printf("%i, %i, %i\n",ABSOLUTE_VALUE(a), ABSOLUTE_VALUE(b), ABSOLUTE_VALUE(c));


    return 0;
    
}
