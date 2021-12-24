#include<stdio.h>
#include"enroll.h"

int main()
{
    /* initial code */
    int a[5] = {1,45,3,6,5};
    int max = a[0];
    for (int i = 1; i < 5; i++)
    {
        /* cheacking the condition */
        if (max < a[i])
        {
            /* Assigning the largest value to max */
            max = a[i];
        }
    }
    printf("The largest number is : %d\n",max);
    return 0;
}
