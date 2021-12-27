#include<stdio.h>

/* Initilizing the fuinctions */
void display();

/* main function */
int main()
{
    /* code */
    int numbers[5] = {1,2,3,4,5};
    display(numbers); 
    return 0;
}

/* Defining the function */
void display(int num[5])
{
    for (int i = 0; i < 5; i++)
    {
        /* code */
        printf("%d ",num[i]);
    }
    printf("\n"); 
}