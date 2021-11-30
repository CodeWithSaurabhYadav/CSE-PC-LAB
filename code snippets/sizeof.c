#include<stdio.h>

int main()
{
    /* code */
    printf("Size of the datatype on the machine (way1) : \n");
    printf("int : %lu\n",sizeof(int));
    printf("char : %lu\n",sizeof(char));
    printf("volid : %lu\n",sizeof(void));
    printf("float : %lu\n",sizeof(float));

    printf("\nSize of the datatype on the machine (way2): \n");
    printf("int : %lu\n",sizeof(int[5]));
    printf("char : %lu\n",sizeof(char[5]));
    printf("volid : %lu\n",sizeof(void));
    printf("float : %lu\n",sizeof(float[20]));

    printf("\nSize of the defined variables on the machine : \n");
    int val1 = 5;char val2 = "Hello"; float val3 = 52.5;
    printf("int : %lu\n",sizeof(val1));
    printf("char : %lu\n",sizeof(val2));
    printf("float : %lu\n",sizeof(val3));
}
