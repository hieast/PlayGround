#include <stdio.h>
#include <stdbool.h>

int main (void)
{
    int a, b;
    printf ("Enter two integer:");
    scanf ("%i%i", &a, &b);
    
    printf ("The fisrt number can%c divide exactly by the second number.\n", 
        (a % b)?'t':' ');
    
    return 0;
}