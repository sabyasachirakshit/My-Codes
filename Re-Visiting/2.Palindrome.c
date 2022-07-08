#include<stdio.h>
int main(int argc, char const *argv[])
{
    char string[100];
    int len_of_string=0,flag=1;
    printf("Enter String: ");
    gets(string);
    for(int i=0;string[i]!='\0';i++){
        len_of_string++;
    }
    for(int i=len_of_string-1,j=0;i!=-1,string[j]!='\0';i--,j++){
        if(string[i]!=string[j]){
            flag=0;
            break;
        }
    }
    if(flag==0){
        printf("String %s is not palindrome!",string);
    }
    else
        printf("String %s is palindrome!",string);
    return 0;
}
