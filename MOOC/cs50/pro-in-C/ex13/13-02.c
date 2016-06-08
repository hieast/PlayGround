#include <stdio.h>

#define str(x) # x
#define printint(var) printf(#var " = %i\n", var);
#define printx0(n) printf("x[" #n "] = %i\n", x[n]);
#define printx(n) printint(x ## n)



int main (void)
{
    int num = 1000;
    printf (str ("hello"\n));
    printint(num)
    
    int x[] = {0, 1, 2, 3, 4, 5};
    int x2 = 22;
    printx0(2)
    printx(2)
    
    
    return 0;
}