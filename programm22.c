#include<stdio.h>
#include"enroll.h"

int main()
{
    /* code */
    int a[5] = {5,6,1,8,-2};
    int ass;
    for (int i = 1; i < 5; i++)
    {
        /* code */
        for (int j = 0; j < 5; j++)
        {
            /* code */
            if (a[j] < a[i])
            {
                /* code */
                ass = a[j];
                a[j] = a[i];
                a[i] = ass;
            }
            
        }
        
    }
    
    return 0;
}
