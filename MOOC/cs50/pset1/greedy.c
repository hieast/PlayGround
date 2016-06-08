#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    printf("O hai! ");
    float dollar;
    int cent;
    do
    {
        printf("How much change is owed?\n");
        dollar =  GetFloat();
    }
    while(dollar < 0);
    cent = round(dollar * 100);
    //printf("%d\n", cent);
    printf("%d\n", cent/25 + cent%25/10 + cent%25%10/5 + cent%25%10%5);
}