#include<stdio.h>

void first();
int val();

int main()
{
    /* code */
    first();
    printf("\n%d\n",val());
    return 0;
}
void first()
{
    printf("\nHello word\n");
}
int val()
{
    int value = 45;
    return value;
}
