#include <iostream>

using namespace std;
bool should_bob_work=false;
void merge(long long arr[], int p, int q, int r) {
  
  int n1 = q - p + 1;
  int n2 = r - q;

  long long L[n1], M[n2];

  for (int i = 0; i < n1; i++)
    L[i] = arr[p + i];
  for (int j = 0; j < n2; j++)
    M[j] = arr[q + 1 + j];

  
  int i, j, k;
  i = 0;
  j = 0;
  k = p;

  
  while (i < n1 && j < n2) {
    if (L[i] <= M[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = M[j];
      j++;
    }
    k++;
  }

  
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = M[j];
    j++;
    k++;
  }
}


void mergeSort(long long arr[], int l, int r) {
  if (l < r) {
    
    int m = l + (r - l) / 2;

    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    
    merge(arr, l, m, r);
  }
}
void give_answer(long long* array, int n, long long k,int left,int right){
    while(left<=right){
        if(left==right && should_bob_work==true){
            cout<<left<<endl;
            return;
        }
    long long answer=(left+right)/2;
    long long temp=0;
    for(int i=0;i<n;i++){
        if(array[i]<answer){
            continue;
        }
        else{
           // printf("hello\n");
            long long sum1=((answer)*(answer+1))/2;
            
            long long sum2=((array[i])*(array[i]+1))/2;
            
            temp=temp-sum1;
            temp=temp+sum2;
        }
    }
    //cout<<temp<<endl;
    if(temp>k){
        left=answer+1;
        should_bob_work=false;
        give_answer(array,n,k,left,right);
        return;
    }
    else if(temp==k){
        cout<<answer<<endl;
        return;
    }
    else{
        //printf("Hello\n");
        right=answer;
        should_bob_work=true;
        give_answer(array,n,k,left,right);
        return;
    }
    }
}
int main(){
    int test;
    cin>>test;
    for(int i=0;i<test;i++){
        int n;
        long long k;
        cin>>n>>k;
        long long array[n];
        for(int i=0;i<n;i++){
            cin>>array[i];
        }
        mergeSort(array,0,n-1);
        give_answer(array,n,k,0,1e8);
    }
    return 0;
}
   
