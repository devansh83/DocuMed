#include <iostream>
using namespace std;
long long max=998244353;

long long final_result[20][20];
long long sample[20][20];
void multiply_inputs(long long (*matrix1)[20],long long (*matrix2)[20],int k){
    long long max=998244353;
    for(int i=0;i<k;i++){
        for(int j=0;j<k;j++){
            long long temp=0;
            for(int l=0;l<k;l++){
                long long temp1=(matrix1[i][l])*(matrix2[l][j])%max;
                temp+=temp1;
                temp=temp%max;
            }
            sample[i][j]=temp;
        }
    }
    return;
}
void give_answer(long long (*matrix) [20],long long power, int k){
    if(power==1){
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                final_result[i][j]=matrix[i][j];
            }
        }
        return;
    }
    give_answer(matrix, power/2,k);
    multiply_inputs(final_result,final_result,k);
    if(power%2==0){
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                final_result[i][j]=sample[i][j];
            }
        }
        
    }
    else{
        long long sample2[20][20];
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                sample2[i][j]=sample[i][j];
            }
        }
        multiply_inputs(sample2,matrix,k);
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                final_result[i][j]=sample[i][j];
            }
        }
    }
    return;
}
int main(){
    int test;
    cin>>test;
    for(int i=0;i<test;i++){
        long long n;
        int k;
        cin>>n>>k;
        if(n<k){
            k=n;
        }
        long long array[k];

        array[0]=1;
        for(int i=1;i<k;i++){
            long long temp=0;
            for(int j=0;j<i;j++){
                temp+=array[j];
            }
            array[i]=temp;
        }
        
        long long matrix_a[20][20];
        for(int i=0;i<k;i++){
            for(int j=0;j<k;j++){
                if(i==0){
                    matrix_a[0][j]=1;
                }
                else if(i==(j+1)){
                    matrix_a[i][j]=1;
                }
                else{
                    matrix_a[i][j]=0;
                }
            }
        }
        give_answer(matrix_a,n-k+1,k);
        long long max=998244353;
        long long answer=0;
        for(int i=0;i<k;i++){
            long long answer1=((final_result[0][i])*(array[k-1-i]))%max;
            answer+=(answer1);
            answer=answer%max;
        }
        
       
        
        cout<<(answer%max)<<endl;
    }
   
    return 0;
}

