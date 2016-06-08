#include <stdio.h>

struct entry
{
    int value;
    struct entry *before;
    struct entry *next;
};

void insertEntry(struct entry *to, struct entry *insert)
{
    insert->next = to->next;
    insert->before = to;
    to->next = insert;
    insert->next->before = insert;
    
}

void printEntry(struct entry *list_pointer)
{
    list_pointer = list_pointer->next;
    while (list_pointer != (struct entry *)0){
        printf ("%i  ", list_pointer->value);
        list_pointer = list_pointer->next;
    }
    printf ("\n");
}
    
void removeEntry(struct entry *removed)
{
    
    removed->before->next = removed->next;
    
}

int main (void)
{
    struct entry start, n1, n2, n3, n4;
    
    start.next = &n1;
    start.value = 0;
    start.before = 0;
    
    n1.value = 100;
    n1.before = &start;
    n1.next = &n2;
    
    n2.value = 200;
    n2.before = &n1;
    n2.next = &n3;
    
    n3.value = 300;
    n3.before = &n2;
    n3.next = 0;
    
    n4.value = 50;
    n4.before = 0;
    n4.next = 0;
    
    printEntry(&start);
    insertEntry(&start, &n4);
    printEntry(&start);
    removeEntry(&n4);
    printEntry(&start);
    
    return 0;
}