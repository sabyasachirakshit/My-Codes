#include<iostream>
using namespace std;
int main(){
    int A[100],len;
    cout<<"Enter size of array: "<<endl;
    cin>>len;
    for(int i=0;i<len;i++){
        cout<<"Enter element "<<i+1<<" :"<<endl;
        cin>>A[i];
    }
    for(int i=0;i<len;i++){
        if((i+1)%2!=0){
            cout<<A[i];
        }
    }
    return 0;
}