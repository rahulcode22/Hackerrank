#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t;
   cin >> t; 
    for(int a0 = 0; a0 < t; a0++)
    { int n,x; int count=0; 
     cin >> n; 
      int flag=n;
     while(flag>0)
        {

            x=flag%10;
                if( x!=0 && n%x==0) 
                {
                    count++;
                }
                /*if(x==0)
                    {
                    flag=flag/10;
                    x=flag%10;
                    count++;
                    }*/

                flag=flag/10;


        }

    cout<<count<<"\n";
}
    return 0;
}
