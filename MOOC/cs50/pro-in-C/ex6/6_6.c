// Program to convert digits to English.

#include <stdio.h>

int main(void)
{
    int number, reverse_num = 0, right_digit;
    
    printf ("Enter your number.\n");
    scanf ("%i", &number);
    
    //deal negative number
    if (number < 0)
    {
        printf ("negative ");
        number = -number;
    }
    // reverse number
    
    while ( number != 0)
    {
     right_digit = number%10;
     reverse_num = reverse_num * 10 + right_digit;
     number /= 10;
    }
    
    do
    {
     right_digit = reverse_num%10;
    switch (right_digit)
    {
        case 0:
            printf ("zero ");
            break;
        case 1:
            printf ("one ");
            break;
        case 2:
            printf ("two ");
            break;
        case 3:
            printf ("three ");
            break;
        case 4:
            printf ("four ");
            break;
        case 5:
            printf ("five ");
            break;
        case 6:
            printf ("six ");
            break;
        case 7:
            printf ("seven ");
            break;
        case 8:
            printf ("eight ");
            break;
        case 9:
            printf ("nine ");
            break;
        default:
            printf ("Undefined input");
     }
     reverse_num /= 10;
    }
    while ( reverse_num != 0);
    
    printf ("\n");
    
    return 0;
}