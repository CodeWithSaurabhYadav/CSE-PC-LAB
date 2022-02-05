/*
Question:
Write a C code that swaps two integers using a user defined function named
swap() with the help of reference of the variable in which the user has entered integers
through the keyboard.
*/

#include<stdio.h>
//EnrollmentNumber_202103103510362

//Initalizing the Swap Function
void swap();

//This is the main function of the program
int main()
{
    /* code */
    //Initilizing the two integer variables
    int num1; int num2;
    printf("Enter the two numbers (a,b) : ");
    //Reading the users entered numbers
    scanf("%d,%d",&num1,&num2);
    //Passing the user entered number through the swap function
    swap(&num1,&num2); //&num1 and &num2 are the reference variables
    //Printing the swapped values
    printf("The swapped numbers are : %d, %d\n",num1,num2);
    return 0;
}

//Defination of the swap
void swap(int *num1ref, int *num2ref) //Here are the 2 pointer variables that acceptes the address of the num1 and num2 resp..
{
    /* code */
    //swaping the the reference of the user entered number
    //Creating the temporary variable to swap the values
    int temp = 0;
    /* Code for swapping the valuesn */
    temp = *num1ref;
    *num1ref = *num2ref;
    *num2ref = temp;
}