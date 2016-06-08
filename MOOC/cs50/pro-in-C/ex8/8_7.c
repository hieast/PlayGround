#include <stdio.h>

long int x_to_the_n(int x, int n)
{
    if (n == 0)
        return 1;
    else
        return x * x_to_the_n(x, n-1);
}

int main(void)
{
    printf ("3^2 = %li\n", x_to_the_n(3,2));
    printf ("4^0 = %li\n", x_to_the_n(4,0));
    printf ("2^10 = %li\n", x_to_the_n(2,10));
    
    return 0;
}