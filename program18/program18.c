#include<stdio.h>
#include"enroll.h"

int main()
{
    //Enroll
    enroll_print();
    /* code */
    int num;
    printf("Enter the number : ");scanf("%d",&num);
    for (int i = 0; i < num; i++)
    {
        /* code */
        for (int j = 0; j <= i ; j++)
        {
            /* code */
            printf("*");
        }
        printf("\n");   
    }
    return 0;
}
