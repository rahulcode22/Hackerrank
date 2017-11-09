#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
using namespace std;


int main(){
    int n;
    float p=0.0,z=0.0,N=0.0;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
     for(int arr_i = 0;arr_i < n;arr_i++){
                if(arr[arr_i]>0)
                   {
                       p++;
                   }
         else if(arr[arr_i]<0)
             {
             N++;
         }
         else
             {
             z++;
         }
    }
    float d1=p/n;
    float d2=N/n;
        float d3=z/n;

      cout<<setprecision(4)<<d1<<endl;
      cout<<setprecision(4)<<d2<<endl;
      cout<<setprecision(4)<<d3<<endl;






    return 0;
}
