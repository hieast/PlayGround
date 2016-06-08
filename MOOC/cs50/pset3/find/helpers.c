/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // for(int i=0; i < n; ++i){
    //     if (values[i] == value)
    //         return true;
    // }
    // return false;

    int lower = 0, upper = n, mid = n/2;
    while (lower < upper){
        if (value == values[mid]){
            return true;
        }
        else if (value > values[mid]){
            lower = mid + 1;
            mid = (lower + upper) / 2;
        }
        else{
            upper = mid;
            mid = (lower + upper) / 2;
        }
    }
    
    return false;
}

/**
 * Sorts array of n values.
 */


void sort(int *array, int n)
{
    if (n > 1){
        sort(array, n / 2);
        sort(array + n / 2, n - n / 2);
        
        int cpar[n / 2];
        for(int i = 0; i < n / 2; ++i)
            *(cpar + i) = *(array + i);
        int i, j;
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
    return;
}