#include <stdio.h>

int main (void)
{
    float value, memory = 0;
    char operator;
         
    printf ("Begin Calculations\n");
        
    while (1)
    {
   
        scanf ("%f %c", &value, &operator);

        switch (operator)
        {
            case 'S':
                memory = value;
                printf ("= %.6f\n", memory);
                break;
            case 'E':
                printf ("= %.6f\n", memory);
                printf ("End of Calculations\n");
                break;
            case '+':
                memory +=  value;
                printf ("= %.6f\n", memory);
                break;
            case '*':
            case 'x':
                memory *=  value;
                printf ("= %.6f\n", memory);
                break;
            case '-':
                memory -=  value;
                printf ("= %.6f\n", memory);
                break;
            case '/':
                if (value == 0)
                    printf ("Division by zero.\n");
                else
                {
                    memory /=  value;
                    printf ("= %.2f\n", memory);
                }
                break;
            default:
                printf ("Unknown operator.\n");
                break;
                
        }
        if (operator == 'E')
            break;
    }
    return 0;
    
}