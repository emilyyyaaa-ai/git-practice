#include <iostream>
using namespace std;
int main()
{
    long long a = 0, b = 1;
    //输出不超过1000的斐波那契数
    while(a <= 1000)
    {
        cout<<a<<endl;
        long long next = a + b;
        a = b;
        b = next;
    }
    return 0;
}