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
    int a0;
    int a1;
    int a2;
    int ap=0,ab=0;
    cin >> a0 >> a1 >> a2;
    int b0;
    int b1;
    int b2;
    cin >> b0 >> b1 >> b2;
    if(a0!=b0) {a0>b0 ? ap+=1 :ab+=1;}
    if(a1!=b1) {a1>b1 ? ap+=1 :ab+=1;}
    if(a2!=b2) {a2>b2 ? ap+=1 :ab+=1;}
    cout<<ap<<" "<<ab;

    return 0;
}
