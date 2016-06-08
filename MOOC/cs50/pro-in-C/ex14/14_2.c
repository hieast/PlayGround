#include <stdio.h>

enum month {Jan = 1, Feb, Mar, Apr, May, Jue, Jul, Aug, Sep, Oct, Nov, Dec};

char * monthName(enum month aMonth)
{
    char * month_name[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jue", "Jul",
                         "Aug", "Sep", "Oct", "Nov", "Dec"};
    return month_name[aMonth - 1];
}




int main (void)
{
    enum month aMonth = 11;
    printf ("%i, %s\n",aMonth, monthName(aMonth));
    return 0;
}