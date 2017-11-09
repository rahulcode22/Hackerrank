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
    int n,cnt=0;
    cin >> n;
    string B;
    cin >> B;
    for(int i=0;i<n;i++)
        {
            if((B[i]=='0') && (B[i+1]=='1') && (B[i+2]=='0'))
                {
                cnt++;
                i+=2;
            }
        }
    cout<<cnt<<endl;
    return 0;
}
