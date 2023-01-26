#include<iostream>
using namespace std;
main(int argc, char const *argv[])
{
    string u_string;
    int len_of_string=0;
    cout<<"Enter string:";
    cin>>u_string;
    cout<<"\nGiven String: "<<u_string;
    for(int i=0;u_string[i]!='\0';i++){
        len_of_string++;
    }
    cout<<"\n\nReverse of string "<<u_string<<" is: \n";
    for(int j=len_of_string;j!=-1;j--){
        cout<<u_string[j];
    }
    return 0;
}

