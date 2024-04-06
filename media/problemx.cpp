#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int maximum( int a , int b)
{
    if(a>b) return a;
    return b;
}

void calculatedepth( int* result, int maxindex[][10], int n, int i, int j, int d)
{
    if(i==j)
    {
        result[i]=d;
        return;
    }
    if(i>j)
    {
        return;
    }
    int index;
    int len = (int)log2(j-i+1);
    if(pow(2,len)==j-i+1)
    {
        index=maxindex[i][len];
    }
    else
    {
        int a=maxindex[i][len]; 
        int b=maxindex[j-(int)pow(2,len)+1][len];
        if(result[a]<result[b])
        {
            index=b;
        }
        else
        {
            index=a;
        }
    }
    result[index]=d;
    calculatedepth(result,maxindex,n,i,index-1,d+1);
    calculatedepth(result,maxindex,n,index+1,j,d+1);
}

void solve()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int max[n][10];
    for (int j = 0; j <= (int)log2(n); j++)
    {
        for (int i = 0; i < n; i++)
        {
            if(j==0)
            {
                max[i][j]=i;
            }
            else if(i+pow(2,j)<=n)
            {
                int a=max[i][j-1];
                int b=max[i + (int)(pow(2,j-1))][j-1];
                if(arr[a]<arr[b])   max[i][j]=b;
                else    max[i][j]=a;
            }
        }
    }
    int depth[n];
    calculatedepth(depth,max,n,0,n-1,0);
    for (int i = 0; i < n; i++)
    {
        cout << depth[i]<<" ";
    }
    cout << endl;
      
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    
}