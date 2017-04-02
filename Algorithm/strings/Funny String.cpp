#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n,count;
    cin>>n;
    string s,r;
    
    while(n--)
        {
		count=0;
        cin>>s;

        r=s;
        reverse(r.begin(),r.end());
        for(int j=1;j<s.length();j++)
            {
             if(abs(s[j]-s[j-1])==abs(r[j]-r[j-1]))
            {count++;

            }
            }
        
    if(count==s.length()-1)
        {
        cout<<"Funny"<<endl;
    }
    else
        {
        cout<<"Not Funny"<<endl;
    }
    }
    return 0;
}
