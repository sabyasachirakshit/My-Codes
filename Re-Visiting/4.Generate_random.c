#include<stdio.h>
#include<stdlib.h>
int main(int argc, char const *argv[])
{
    int lower=100,upper=1000;
    for(int i=0;i<5;i++){
        int num = (rand()%(upper - lower + 1)) + lower;
        printf("%d",num);
    }
    
    return 0;
}
