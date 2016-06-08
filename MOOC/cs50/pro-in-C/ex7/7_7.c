// Sieve of Erastosthenes

#include <stdio.h>

int main(void)
{
    int P[5000] = {}, num = 150;
    
    printf ("What the upper bound of the prime? ");
    scanf ("%i", &num);
    

    for (int i = 2; i <= num ;i++){
        for (int j = i; i * j <= num; j++){
            P[i * j] = 1;
        }
    }
    
    for (int i = 2; i <= num; i++){
        if (!P[i])
            printf ("%i ", i);
    }
    printf ("\n");
    return 0;
}