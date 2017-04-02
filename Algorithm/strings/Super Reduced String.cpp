#include <iostream>
#include<string>
using namespace std;
string rem(string a){
    for(int i=0;i<a.size();)
        {
            if(a[i] == a[i+1])
                {
                    a.erase(i,2);
                }else if(a[i-1] == a[i] && i != 0){
                    a.erase(i-1,2);
                }else{
                    i++;
                }
        }
        if(a.size() == 0){
            return "Empty String";
        }else{
            return a;
        }
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string str,ans;
    cin>>str;
    ans = rem(str);
        cout<<rem(ans)<<endl;
    return 0;
}
