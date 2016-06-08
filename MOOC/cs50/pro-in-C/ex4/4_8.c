#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    int i, j, next_multiple;
    i = atoi(argv[1]);
    j = atoi(argv[2]);
    next_multiple = i + j - i % j;
    
    printf ("next_multiple = %i\n", next_multiple);
    
    return 0;
    
}