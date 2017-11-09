#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin>>t;
    string s;

    for(int i=0;i<t;i++)
        {
            cin>>s;
             int cnt=0;
           for(int j=0;j<s.length();j++)
               {
                    if(s[j]==s[j+1])
                    {
                    cnt++;
                    }
                }
        cout<<cnt<<endl;
           }
    return 0;
}
