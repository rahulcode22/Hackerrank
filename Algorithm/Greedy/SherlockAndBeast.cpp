#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
int t;
cin >> t;
for(int a0 = 0; a0 < t; a0++)
{

int n, y, z, flag = -1;
 cin >> n;
z = n;
 if(z <= 0)
    cout<<"-1\n";
    else
    {
        if(z%3 == 0)
            {
            cout<< string(z,'5')<<"\n";
            }
    while(z%3 != 0)
    {
        z -= 5;
        if(z<0)
            {
            cout<<"-1\n";
                break;
            }
    else
            {
            if(z%3==0)
             cout<<string(z,'5')<<string((n-z),'3')<<"\n";
             }
    }


    }
    }
return 0;
}
