#include <stdio.h>

void swap(int * const a, int *const b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


void printArray(int *array, int n)
{
    for(int i = 0 ; i < n; ++i){
        printf ("%i ",array[i]);
    }
    printf ("\n");
}

void copyArray(int *array, int *cpar, int n)
{
    for(int i = 0; i < n; ++i)
        *(cpar + i) = *(array + i);
}

void mergeSort(int * const array, int n)
{
    printArray(array, n);
    if (n > 1){
        mergeSort(array, n / 2);
        mergeSort(array + n / 2, n - n / 2);
        
        int cpar[n / 2], i, j;
        copyArray(array, cpar, n / 2);
        for (i = 0, j = 0; i < n / 2 && j < n - n / 2;){
            if (*(cpar + i) < *(array + n / 2 + j)){
                *(array + i + j) = *(cpar + i);
                ++i;
            }
            else{
                *(array + i + j) = *(array + n / 2 + j);
                ++j;
            }
        if (j == n - n /2) {
            while(i < n / 2){
                *(array + i + j) = *(cpar + i);
                ++i;
            }
        }
        }
    }
    printArray(array, n);
}

int main(void)
{
    int array[] = {9,8,7,6,5,4,3,2,1,0};
    printArray(array, 10);
    swap(array, array + 1);
    printArray(array, 10);
    mergeSort(array, 10);
    printArray(array, 10);

    return 0;
}