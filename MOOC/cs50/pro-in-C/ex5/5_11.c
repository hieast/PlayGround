#include <stdio.h>

int main(void)
{
    int num, sum = 0, temp;
    printf ("Enter a integer: ");
    scanf ("%i", &num);
    
    printf ("The sum of digits of %i is ", num);
    while (num != 0)
    {
        temp = num % 10;
        sum += temp;
        num /= 10;
    }
    printf ("%i\n", sum);
    
    return 0;
}