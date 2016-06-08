#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    float F, C;
    F = atoi(argv[1]);
    C = (F - 32) / 1.8;
    printf ("%g F is eaqul to %g C.\n", F, C);
    return 0;
    
}