#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string name = GetString();
    bool isFirst = 1;
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        if(name[i] == ' ')
        {
            isFirst = 1;
        }
        else if(isFirst == 1)
        {
            printf("%c", toupper(name[i]));
            isFirst = 0;
        }
    }
    printf("\n");
    return 0;
}