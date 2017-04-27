#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int t;
    float a,b;
    scanf("%d",&t);
    while(t--)
        {
        scanf("%f %f",&a,&b);
        a=ceil(sqrt(a));
        b=floor(sqrt(b));
        printf("%d\n",(((int)(b-a))+1));
    }
    return 0;
}
