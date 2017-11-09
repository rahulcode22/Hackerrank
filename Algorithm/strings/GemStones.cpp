#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
     int rocks;
    cin>>rocks;
    string letter;
    int count = 0;
    for (int r = 0; r < rocks; r++) {
        string s;
        cin>>s;
        for (int i = 0; i < s.length(); i++) {

            if (letter[s[i] - 'a'] == r) {
                letter[s[i]- 'a']++;
                if (letter[s[i]- 'a'] == rocks) {
                    count++;
                }
            }
        }
    }

    cout<<count<<endl;
    return 0;
}
