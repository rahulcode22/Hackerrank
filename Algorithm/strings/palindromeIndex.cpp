#include<iostream>
#include<string>
using namespace std;
int main(){
    int r,a;
    cin>>r;
    while(r--)
        {
            string z;
            cin>>z;
            int q=z.size();
            for( a=0;a<=(q/2);a++)
                {
                    if(z[a]!=z[q-1-a])
                        {
                             if((z[a+1]==z[q-1-a])&&(z[a+2]==z[q-1-a-1]))
                            cout<<a<<endl;
                           else if((z[a]==z[q-1-a-1])&&(z[a+1]==z[q-1-a-2]))
                            cout<<q-1-a<<endl;
                            goto jump;

                        }
                }
                cout<<"-1"<<endl;
      jump:;
        }
    return 0;
}
