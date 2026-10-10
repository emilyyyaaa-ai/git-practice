#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "请输入一个整数：";
    cin >> n;
    if (n % 2 == 0)
    {
        cout << n <<"是偶数。" << endl;
    }
    else
    {
        cout << n <<"是奇数。" << endl;
    }
    return 0;
}