#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    string S;
    cin >> S;
    int count=0;
    for(int i=0;i<S.length();i++)
        {
              
        if(i%3==1)
                {
                if(S[i]!='O')
                    {
                    count++;}
            }
            else if((i%3==0) ||(i%3==2))
                {
                    if(S[i]!='S')
                    {
                        count++;
                    }
            }
                
     
        }
     cout<<count<<endl;
    
    
    return 0;
}
