/*
Task 1 - The data file named data.txt has been attached with the post. You need to
develop a C program that extracts the last three digits of the student enrollment
number from our institute email id format and generates a new file with name
enrollment.txt having full 15 Digit Enrollment number i.e. 202103103510001.
[You need to add the last three digits extracted from the file data.txt with prefix
sequence 202103103510 and generate a full 15 digit enrollment number.]

Input: Read data.txt from the C program.
Output: Generate new file enrollment.txt having 15 digit enrollment numbers (each
in new line) of student whose id is present in data.txt.
*/

#include<stdio.h>

int main()
{
    // Opening the files
    FILE *data = fopen("data.txt","r");
    FILE *enroll = fopen("enrollment.txt","w");
    char str[100];
    // Reading the lines of the data.txt
    while (fgets(str,sizeof(str),data))
    {
        printf("%s",str);
        // Initilizing the arrays
        char sufix[4];
        // Defining the prefix
        char prefix[14] = "202103103510";
        /* Extracting the 3 numbers form institute
        id and palcing them into a new variable*/
        sufix[0] = str[8];
        sufix[1] = str[9];
        sufix[2] = str[10];
        // Concating the strings
        strcat(prefix,sufix);
        // Writig the new enrollment number into enrollment.txt
        fputs(prefix,enroll);
        fputs("\n",enroll);
    }
    //Closing the files
    fclose(data);
    fclose(enroll);
    return 0;
}