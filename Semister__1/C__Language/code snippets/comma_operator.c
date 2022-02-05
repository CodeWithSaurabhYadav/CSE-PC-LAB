#include<stdio.h>

void main()
{
    /* code */
    int num1, num2;
    num1 = (num2 = 3, num2 = num2 + 5); 
    /*
    first value is assigned to num2 as 3 and then it is
    incremented by 5 and the final value is operated to num1
    */
    printf("%d\n",num1);
}
