#include<stdio.h>
int main(int argc, char const *argv[])
{
    int A[100],len;
    printf("Enter size of array: ");
    scanf("%d",&len);
    for(int i=0;i<len;i++){
        printf("Enter element %d: ",i+1);
        scanf("%d",&A[i]);
    }
    for(int i=0;i<len;i++){
        if((i+1)%2!=0){
            printf("%d",A[i]);
        }
    }
    return 0;
}
