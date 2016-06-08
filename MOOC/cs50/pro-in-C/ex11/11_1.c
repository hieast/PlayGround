#include <stdio.h>

struct entry
{
    int value;
    struct entry *next;
};

void insertEntry(struct entry *to, struct entry *insert)
{
    insert->next = to->next;
    to->next = insert;
}

void printEntry(struct entry *list_pointer)
{
    while (list_pointer != (struct entry *)0){
        printf ("%i \n", list_pointer->value);
        list_pointer = list_pointer->next;
    }
}
    

int main (void)
{
    struct entry n1, n2, n3, n4;
    struct entry *list_pointer = &n1, *to = &n2, *insert = &n4;
    
    n1.value = 100;
    n1.next = &n2;
    
    n2.value = 200;
    n2.next = &n3;
    
    n3.value = 300;
    n3.next = (struct entry *)0;
    
    n4.value = 250;
    n4.next = 0;
    
    printEntry(list_pointer);
    insertEntry(to, insert);
    printEntry(list_pointer);
    
    return 0;
}