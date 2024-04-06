#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
long long count(int* array, int n, int start,int mid, int end,int* sample){
    int begin1=start;
    
    int begin2=mid+1;
    
    int check=0;
    long long temp=0;
    while(begin1<=mid && begin2<=end){
        if(array[begin1]<=array[begin2]){
            sample[check]=array[begin1];
            begin1++;
            check++;
        }
        else{
            temp=temp+mid-begin1+1;
           //printf("hello\n");
            sample[check]=array[begin2];
            begin2++;
            check++;
        }
    }
    while(begin1<=mid){
        sample[check]=array[begin1];
        check++; begin1++;
    }
    while(begin2<=end){
        sample[check]=array[begin2];
        check++; begin2++;
    }
    
    return temp;
}
long long inversions(int* array, int n, int start, int end){
    if(start==end) return 0;
    int mid=(start+end)/2;
    int sample[n];
    long long count1=inversions(array,n,start,mid);
    long long count2=inversions(array,n,mid+1,end);
    long long count3=count(array,n,start,mid,end,sample);
    for(int i=start;i<=end;i++){
        array[i]=sample[i-start];
    }
    //printf("%d\n",count3);
    return count1+count2+count3;
}
int main(){
    int test;
    cin>>test;
    for(int i=0;i<test;i++){
        int n;
        cin>>n;
        int array[n];
        for(int j=0;j<n;j++){
            cin>>array[j];
        }
        //int sample[n];
        cout<<inversions(array,n,0,n-1)<<endl;
        //cout<<count(array,n,3,3,4,sample)<<endl;
    }

    return 0;
}