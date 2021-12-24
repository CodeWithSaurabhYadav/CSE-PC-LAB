#include<stdio.h>
#include"enroll.h"

int main()
{
    /* initial code */
    int a[5] = {2,45,1,-6,5};
    int max = a[0];
    // Largest
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
    // Smallest
    int min = a[0];
    for (int j = 1; j < 5; j++)
    {
        /* code */
        if (min > a[j])
        {
            /* code */
            min = a[j];
        }
    }
    printf("The smallest number is : %d\n",min);
    

    return 0;
}
