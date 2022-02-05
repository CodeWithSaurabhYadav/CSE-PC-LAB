#include<stdio.h>
#include"enroll.h"

int main(float first_num,char operator,float sec_num)
{
    //enroll
    enroll_print();
    /* code */
    printf("Enter first number : ");
    scanf("%f",&first_num);
    printf("Enter second number : ");
    scanf("%f",&sec_num);
    printf("Enter the operator(/,*,+,-) : ");
    scanf("\n%[^\n]c",&operator);
    switch (operator)
    {
    case '/':
        printf("\nThe Sum of %f and %f is %.4f\n",first_num,sec_num,first_num/sec_num);
        break;
    
    case '*':
        printf("\nThe Sum of %f and %f is %.4f\n",first_num,sec_num,first_num*sec_num);
        break;
    
    case '+':
        printf("\nThe Sum of %f and %f is %.4f\n",first_num,sec_num,first_num+sec_num);
        break;
    
    case '-':
        printf("\nThe Sum of %f and %f is %.4f\n",first_num,sec_num,first_num-sec_num);
        break;
    
    default:
        printf("\nYou have entered wrong operator/values\n");
        break;
    }
    return 0;
}