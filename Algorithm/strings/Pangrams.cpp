#include <cmath>
#include <cstdio>
#include <vector>
#include<string>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{ 
    int mask[26];
    int i;
    string s;
    int sum=0;
    getline(cin,s);
    int size=s.size();
    for(i=0;i<size;i++)
        {
            s[i]=tolower(s[i]);
        }
    for(i=0;i<size;i++)
        {
            if(s[i]==' ')
                continue;
            else if(s[i]>='a'&&s[i]<='z')
                    {
                        mask[s[i]-'a']=1;
                    }
        }
    for(i=0;i<26;i++)
        {
            sum+=mask[i];
        }
    if(sum==26)
        cout<<"pangram";
    else
        cout<<"not pangram";


  return 0;
}
