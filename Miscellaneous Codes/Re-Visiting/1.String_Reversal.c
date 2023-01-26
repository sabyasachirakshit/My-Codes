#include<stdio.h>
int main(int argc, char const *argv[])
{
    char string[100];
    int len_of_string=0;
    printf("Enter String: ");
    gets(string);
    printf("\nGiven String: %s ",string);
    for(int i=0;string[i]!='\0';i++){
        len_of_string++;
    }
    printf("\n\nReverse of string %s is: \n");
    for(int i=len_of_string;i!=-1;i--){
        printf("%c",string[i]);
    }
    return 0;
}
