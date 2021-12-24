#include<stdio.h>
#include"enroll.h"

int main()
{
    //Enroll
    enroll_print();
    /* code */
    int num;
    printf("Enter the number : ");scanf("%d",&num);
    /* Patten 1 Left Triangle of * */
    printf("Patter 1\n");
    for (int i = 1; i < num+1; i++)
    {
        /* code */
        for (int j = 1; j <= i ; j++)
        {
            /* code */
            printf("* ");
        }
        printf("\n");   
    }
    /* Pattern 2 Left Triangle Numbers */
    printf("Patter 2\n");
    for (int k = 1; k < num+1; k++)
    {
        /* code */
        for (int l = 1; l <= k; l++)
        {
            /* code */
            printf("%d ",l);
        }
        printf("\n");
    }
    /* Pattern 3 Pyramid */
    printf("Patter 3\n"); 
    for (int m = 1; m < num; m++)
    {
        /* code */
        for(int n = 1; n <= (num-m)*2; n++)
        {
            printf(" ");
        }
        for(int o = m; o >= 1; o--)
        {
            printf(" *");
        }
        for(int p = 2; p <= m ; p++)
        {
                printf(" *");
        }
        printf("\n");
    }
    
    return 0;
}
