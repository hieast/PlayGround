#include <stdio.h>

int main(void)
{
    long long int Fib1 = 0, Fib2 = 1, Fib3, num;
    printf ("How many Fibonacci do you want? More than 2. ");
    scanf ("%lli", &num);
    
    printf ("The %ith Fib is %lli \n", 1, Fib1);
    printf ("The %ith Fib is %lli \n", 2, Fib2);
    
    for (int i = 2; i < num; i++){
        Fib3 = Fib1 + Fib2 ;
        printf ("The %ith Fib is %lli \n", i + 1, Fib3);
        Fib1 = Fib2;
        Fib2 = Fib3;
    }
    
    printf ("Done!\n");
    
    return 0;

    
}