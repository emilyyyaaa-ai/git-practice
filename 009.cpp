#include <iostream>
using namespace std;

int square(int x)
{
    return x * x;
}

int main()
{
    int n;
    cout << "请输入一个整数: ";
    cin >> n;
    cout << n << " 的平方是: " << square(n) << endl;
    return 0;
}