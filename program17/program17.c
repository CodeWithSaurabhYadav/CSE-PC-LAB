#include<stdio.h>
#include"enroll.h"

int main()
{
    //Enroll
    enroll_print();
    /* code */
    printf("Prime numbers from 1 to 100 are :\n");
    for (int i = 2; i <= 100; i++)
    {
        /* code */
        int count = 0;
        for (int j = 2; j < i/2; j++)
        {
            /* code */
            if (i%j==0)
            {
                /* code */
                count++;
                break;
            }
        }
        if (count==0)
        {
            /* code */
            printf(" %d ",i);
        }      
    }
    printf("\n");        
    return 0;
}
