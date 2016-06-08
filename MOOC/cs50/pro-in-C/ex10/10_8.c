#include <stdio.h>
#include <stdbool.h>

int findString(char string1[], char string2[]) 
{
    int i, j;
    for(i = 0; string1[i] != '\0'; i++){
        for(j = 0; string2[j] != '\0'; j++){
            if (string1[i + j] != string2[j]){
                break;
            }
        }
        if (string2[j] =='\0'){
            return i;    
        }
    }
    return -1;
}

void removeString(char string[], int index, int length)
{
    int i;
    for (i = index; string[i + length] != '\0'; i++){
        string[i] = string[i + length];
    }
    string[i] = '\0';
    
}

void insertString(char string[],char insert[], int index)
{
    int counter1, counter2;
    for (counter1 = 0; string[counter1] != '\0'; counter1++);
    for (counter2 = 0; insert[counter2] != '\0'; counter2++);
    for (int i = counter1 + counter2; i > index + counter2 - 1; i--, counter1--){
        string[i] = string[counter1];
    }
    for (int j = index; j < counter2 + index; j++){
        string[j] = insert[j - index];
    }
    
    
}

bool replaceString(char source[], char s1[], char s2[])
{
    int index = findString(source, s1);
    int length_s1;
    
    if ( index == -1)
        return false;
    else{
        for (length_s1 = 0; s1[length_s1] != '\0'; length_s1++);
        removeString(source, index, length_s1);
        insertString(source, s2, index);
        return true;
    }
    
    
}

int main(void)
{
    printf("findString %i\n", findString("a chatterbox", "hat"));
    char text[] = "the wrong son";
    removeString(text, 4, 6);
    printf("removeStrung %s\n", text);
    insertString(text, "per", 4);
    printf("insertString %s\n", text);
    
    char source[] = "csd1hyh1abc1", s1[] = "1", s2[] = "one";
    printf("before %s\n", source);
    replaceString(source, s1, s2);
    printf("after %s\n", source);
    
    bool stillFound;
    do{
        stillFound = replaceString(source, s1, s2);
    }
    while (stillFound);
    printf("after do-while loop %s\n", source);
    
    return 0;
    
}