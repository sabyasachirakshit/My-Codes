#include<iostream>
using namespace std;
main(int argc, char const *argv[])
{
    string u_string;
    int len_of_string=0,flag=1;
    cout<<"Enter string:";
    cin>>u_string;
    cout<<"\nGiven String: "<<u_string;
    for(int i=0;u_string[i]!='\0';i++){
        len_of_string++;
    }
    for(int i=len_of_string-1,j=0;i!=-1,u_string[j]!='\0';i--,j++){
        if(u_string[i]!=u_string[j]){
            flag=0;
            break;
        }
    }
    if(flag==0){
        cout<<"\nString "<<u_string<<"is not palindrome!";
    }
    else
        cout<<"\nString "<<u_string<<"is palindrome!";
    return 0;
}

