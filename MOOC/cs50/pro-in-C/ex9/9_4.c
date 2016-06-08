#include <stdio.h>

struct date
    {
        int month;
        int day;
        int year;
    } ;

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

int main (void)
{
    struct date date1;
    
    printf ("Enter two date of month/day/year(after 03/01/1900): \n");
    scanf ("%i%i%i", &date1.month, &date1.day, &date1.year);
    
    int week = (calN(date1) - 621049) % 7;
    char* days_of_week[7] = {"Sun", "Mon", "Tues", "Wes", "Thur", "Fri", "Sat"};
    printf ("%s\n", days_of_week[week]);
}