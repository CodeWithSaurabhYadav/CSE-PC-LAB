#include<stdio.h>

void main()
{
    printf("\nConditional Operator Type 1\n");
    int age;
    printf("Enter your age : ");scanf("%d",&age);
    (age>=18)?printf("You are eligible for Voting\n"):printf("You are not eligible for Voting\n");

    printf("\nConditional Operator Type 2\n");
    int num1 = 37 , num2 = 31 ,value;
    value = (num1 > num2)?num1:num2;
    printf("\nGreater number is : %d\n",value);
}
