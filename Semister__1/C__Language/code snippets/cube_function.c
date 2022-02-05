#include<stdio.h>

int cube();
int square();
int expo();

int main()
{
    /* code */
    int num,exp;
    int choice;
    int num3,num4;
    int num1;
    int num2;
    while (1<2)
    {
        printf("1) Square\n2) Cube\n3) Other powers\n0) Exit\n\n");
        printf("Choice : ");scanf("%d",&choice);
        /* code */
        switch (choice)
        {
        case 1:
            printf("Enter your number : ");scanf("%d",&num1);
            printf("The Square of %d is %d\n",num1,square(num1));
            break;
        case 2:
            printf("Enter your number : ");scanf("%d",&num2);
            printf("The cube of %d is %d\n",num2,cube(num2));
            break;
        case 3:
            printf("Enter your number : ");scanf("%d",&num3);
            printf("Enter your power : ");scanf("%d",&num4);
            printf("The answer of %d is %d\n",num3,expo(num3,num4));
            break;
        case 0:
            exit(0);
        default:
            break;
        }
    }
    return 0;
}
int square(int number)
{
    int squ;
    squ = number*number;
    return squ;
}
int cube(int number)
{
    int cub;
    cub = number*number*number;
    return cub;
}
int expo(int number,int power)
{
    int number2;
    number2 = number;
    for (int i = 1; i < power; i++)
    {
        /* code */
        number = number*number2;
    }
    return number;
}