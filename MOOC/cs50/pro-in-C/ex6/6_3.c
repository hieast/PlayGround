#include <stdio.h>
#include <stdbool.h>

int main (void)
{
    int a, b;
    printf ("Enter two integer:");
    scanf ("%i%i", &a, &b);
    
    if (b)
    {
        printf ("The fisrt number divide by the second number is %.3f\n", 
        (float) a / b);
    }
    else
    {
       printf ("Division by zero!");
    }
    return 0;
}