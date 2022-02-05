#include<stdio.h>
#include"enroll.h"

int main()
{
    //enrollment number
    enroll_print();
    /* code */
    int num,check;
    printf("Enter the number to check the divisiblity by 3 :\n");
    scanf("%d",&num);
    check = num%3;
    (check == 0)?printf("The given number is divisible by 3\n"):printf("The given number is not divisible by 3\n");
    return 0;
}
