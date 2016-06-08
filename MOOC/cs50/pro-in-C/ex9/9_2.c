#include <stdio.h>

struct date
    {
        int month;
        int day;
        int year;
    } ;
    
int main (void)
{
    struct date date1, date2;
    int calN (struct date datex);
    
    printf ("Enter two date of month/day/year(after 03/01/1900): \n");
    scanf ("%i%i%i", &date1.month, &date1.day, &date1.year);
    scanf ("%i%i%i", &date2.month, &date2.day, &date2.year);
    
    int N1 = calN(date1);
    int N2 = calN(date2);
    
    printf ("\n%i %i %i\n", N1, N2, N2 - N1);
    
    return 0;
    
}

int calN (struct date datex)
{
    /*printf ("%i %i %i, ", 
    1461 * (datex.month <= 2 ? datex.year - 1: datex.year) / 4, 
    153 * (datex.month <= 2 ? datex.month + 13: datex.month + 1) / 5, 
    datex.day);*/
    
    return 
    1461 * (datex.month <= 2 ? datex.year - 1: datex.year) / 4 + 
    153 * (datex.month <= 2 ? datex.month + 13: datex.month + 1) / 5 + 
    datex.day;
}