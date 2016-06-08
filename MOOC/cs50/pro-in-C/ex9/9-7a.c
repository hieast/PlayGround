#include <stdio.h>

int main (void)
{
    int i;
    struct month
    {
        int numberOfDays;
        char name[4];
    };
    
    const struct month months[12] = 
        {{31, "Jan"}, {29, "Feb"}, 
         {31, "Mar"}, {30, "Apr"} };
         
    printf ("Month Number of Days\n");
    printf ("--------------------\n");
    
    for (i = 0; i < 4; i++){
        printf (" %s %i\n", months[i].name, months[i].numberOfDays);
    }
    
    return 0;
}