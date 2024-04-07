#include <iostream>

using namespace std;

int main(){
    long long test;
    cin>>test;
    for(long long i=0;i<test;i++){
        long long n;
        cin>>n;
        long long array[n];
        for(long long j=0;j<n;j++){
            cin>>array[j];
        }
        long long final_answer[n];
        final_answer[n-1]=array[n-1];
        for(long long j=1;j<n;j++){
            if(final_answer[n-j]>0){
                final_answer[n-j-1]=array[n-j-1]+final_answer[n-j];
            }
            else{
                final_answer[n-j-1]=array[n-j-1];
            }
        }
        for(long long j=0;j<n;j++){
            if(j==n-1){
                printf("%lld",final_answer[j]);
            }
            else{
                printf("%lld ",final_answer[j]);
            }
        }
        printf("\n");
        
    }
    return 0;
}