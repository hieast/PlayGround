#include <stdio.h>

int main(void)
{
    printf("(3.31e-8 * 2.01e-7) / (7.16e-6 + 2.01e-8) = %g\n", 
          (3.31e-8 * 2.01e-7) / (7.16e-6 + 2.01e-8));
           
    double  result;  
  
   result = (3.31e-8 * 2.01e-7) / (7.16e-6 + 2.01e-8);  
   printf ("result = %g\n", result); 
   
   
    return 0;
}