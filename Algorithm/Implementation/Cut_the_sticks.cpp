#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
   sort(arr.begin(),arr.end());
reverse(arr.begin(), arr.end());

while(!arr.empty()){

cout<<arr.size()<<endl;
for(int i = 0; i<arr.size();++i)
    arr[i]-=arr[arr.size()-1];
while(arr.back() ==0 && !arr.empty())
    arr.pop_back();

    }
        return 0;
}
