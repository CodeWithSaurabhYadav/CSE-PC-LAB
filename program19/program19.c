#include<stdio.h>
#include"enroll.h"

//pre defined functions
void swap();

//main function
int main()
{
    //enroll 
    enroll_print();
    /* code */
    int num1,num2;
    printf("Enter two numbers (a,b) : ");
    scanf("%d,%d",&num1,&num2);
    swap(num1,num2);
    return 0;
}
//defination of swap function
void swap(int x,int y)
{
    int TEMP;
    printf("Values before swaping : %d, %d\n",x,y);
    TEMP = x;x = y;y = TEMP;
    printf("Values after swaping : %d, %d\n",x,y);
}
