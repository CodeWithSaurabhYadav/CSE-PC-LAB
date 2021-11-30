#include<stdio.h>
#include"enroll.h"
int main(int argc, char const *argv[])
{
    //enrollment number
    enroll_print();
    /* code */
    int num1 = 10,num2 = 20, num3 = 30,largest;
    largest = num1;
    if (num2 > largest) largest = num2;
    if (num3 > largest) largest = num3;
    printf("The largest value is %d\n",largest);
    return 0;
}
