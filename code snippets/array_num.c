#include<stdio.h>

int main()
{
    /* 1D Array */
    int array1D[5] = {1,2,3,4,5};
    for (int i = 0; i < 5; i++)
    {
        /* code */
        printf("%d ",array1D[i]);
    } 
    printf("\n");
    printf("\n");
    /* 2D array */
    int array2D[2][2] = {{1,2},{2,1}};
    /* loop 1 for rows */
    for (int j = 0; j < 2; j++)
    {
        /* loop 2 for columns */
        for (int k = 0; k < 2; k++)
        {
            /* printing the array values */
            printf("%d ",array2D[j][k]);
        }
    printf("\n");
    } 
    return 0;
}
