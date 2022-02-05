#include<stdio.h>
#include"enroll.h"

int main()
{
    //Enroll
    enroll_print();
    /* code */
    int num1 = 1,num2 = 2,num3 = 3;
    printf("Table of 1\n");
    for (int i = 1; i < 11; i++)
    {
        /* code */
        printf("%d * %d = %d\n",num1,i,num1*i);
    }
    printf("Table of 2\n");
    for (int i = 1; i < 11; i++)
    {
        /* code */
        printf("%d * %d = %d\n",num2,i,num2*i);
    }
    printf("Table of 3\n");
    for (int i = 1; i < 11; i++)
    {
        /* code */
        printf("%d * %d = %d\n",num3,i,num3*i);
    }
    return 0;
}
