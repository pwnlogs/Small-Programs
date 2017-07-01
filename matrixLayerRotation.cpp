#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int n, m;

int min(int a, int b){
    return a<b?a:b;
}

int loop_no(int a, int b){
    return min(min(a,m-1-a), min(b,n-1-b));
}

int arr_pos(int a, int b){
    // if a0M<b0N, Metro-politan distance from Ok(0,0)  
    // Else, Metro-politan distance from Ok(end,end)  
    int k = loop_no(a,b);
    if(b==n-1-k && a==m-1-k){
        return (n-2*k)+(m-2*k)-1-1;
    }
    if( b*(m-1-2*k)+k*(n-1) >= a*(n-1-2*k)+(m-1)*k){
        return a-k+b-k;
    }
    else{
        return (m-k-1)-a + (n-k-1)-b + (n-2*k)+(m-2*k)-1-1;
    }
}


int main() {
        
    int r;
    cin>>m>>n>>r;   // m rows; n cols
    int **a = (int**) malloc(sizeof(int*)*(min(m,n)+1)/2);
    for(int i=0; i<(min(m,n)+1)/2; ++i){
        a[i] = (int*)malloc(sizeof(int)*(2*((m-2*i)+(n-2*i-2))));
    }
    for(int i=0; i<m; ++i){
        for(int j=0; j<n; ++j){
            cin>>a[loop_no(i,j)][arr_pos(i,j)];
        }
    }

    for(int i=0; i<m; ++i){
        for(int j=0; j<n; ++j){
            cout<<a[loop_no(i,j)][
                abs((arr_pos(i,j)+r)
                    %(2*((m-2*loop_no(i,j))
                        +(n-2*loop_no(i,j)-2))))
                ]<<" ";
        }
        cout<<endl;
    }
    
    free(a);

    return 0;
}
