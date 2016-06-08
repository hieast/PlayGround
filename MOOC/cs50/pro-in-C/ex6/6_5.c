// Program to reverse the digits of a number

#include <stdio.h>

int main(void)
{
 int number, right_digit, sign;
 
 printf ("Enter your number.\n");
 scanf ("%i", &number);
 
 if (number < 0)
 {
     sign = 0;
     number = -number;
 }
 
 do
 {
     right_digit = number%10;
     printf ("%i", right_digit);
     number /= 10;
 }
 while ( number != 0);
 
 printf ("%c\n", sign?' ':'-');
 
 return 0;
}