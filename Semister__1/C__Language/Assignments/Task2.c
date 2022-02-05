/*
Question:
Write a C code that scans 10 integers from the user in an array named
user_array in the main() function. Develop an user defined function that accepts
an user_array through calling arguments from the main function and print an array
element by element increment by one.
*/

//Initilizing the IncrementArray  Function
int IncrementArray();

#include<stdio.h>
//EnrollmentNumber_202103103510362

int main()
{
    /* code */
    //Initilizing the user_array variable of size 10
    int user_arary[10];
    printf("Enter the array of 10 Elements :\n");
    //Using 'for' loop scanning the values of the user_array
    for (int i = 0; i < 10; i++)
    {
        /* code */
        scanf("%d",&user_arary[i]);
    }
    //Passing the array through IncrementArray Function
    IncrementArray(&user_arary);
    //Printing the new values of the array
    printf("The Increment array is : \n{ ");
    for (int j = 0; j < 10; j++)
    {
        /* code */
        printf("%d ",user_arary[j]);
    }
    printf("}");
    return 0;
}

//Defination of the IncrementArray Function
int IncrementArray(int Array[])
{
    //Using 'for' loop incrementing the values of the array by 1
    for (int i = 0; i < 10; i++)
    {
        /* code */
        Array[i]++;
    }
    return 0;
}