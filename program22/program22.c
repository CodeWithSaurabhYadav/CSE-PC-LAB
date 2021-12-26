#include<stdio.h>
#include"enroll.h"

// Main Function
int main()
{
    // Enroll
    enroll_print();
    /* code */
    // Initial Array of length 5
    int a[5] = {5,6,1,8,-2};
    int ass; // Temporary array for swaping the values
    // Sorting thE data
    /* loopo1 */
    for (int i = 0 ; i < 5; i++)
    {
        /* loop2 */
        for (int j = i + 1; j < 5; j++)
        {
            /* checking the largest of */
            if (a[i] > a[j])
            {
                /* Swaping the data */
                ass = a[i];
                a[i] = a[j];
                a[j] = ass;
            }         
        }      
    }
    printf("The numbers in assending order is : \n");
    printf("[ ");
    // Printing the assending order array
    for (int k = 0; k < 5; ++k)
    {
        /* code */
        printf("%d ",a[k]);
    }
    printf("]\n");
    // Printing the Desending order array
    printf("The numbers in desending order is : \n");
    printf("[ ");
    for (int l = 4; l >= 0; --l)
    {
        /* code */
        printf("%d ",a[l]);
    }
    printf("]\n");      
    return 0;
}
