 #include<iostream>
using namespace std;

int main ()
{
    int n;
    cout << "请输入一个三位整数：";
    cin >> n;
    // 输入合法性校验，处理非法输入场景
    if (n < 100 || n > 999)
    {
        cout << "输入错误，请输入一个有效的三位正整数！" << endl;
        return 1;
    }
    int hundred = n / 100;
    int ten = (n / 10) % 10;
    int single = n % 10;
    int sum = hundred + ten + single;
    cout << "百位:" << hundred << "，十位:" << ten << "，个位:" << single << "，各位数字之和:" << sum << endl;
    return 0;
}