#include<stdio.h>
#include"enroll.h"

int main()
{
    //Enroll
    enroll_print();
    /* code */
    int num1;
    printf("Enter the number : ");scanf("%d",&num1);
    printf("Table of 1\n");
    for (int i = 1; i < 11; i++)
    {
        /* table 1*/
        printf("%d * %d = %d\n",num1,i,num1*i);
    }
    return 0;
}
