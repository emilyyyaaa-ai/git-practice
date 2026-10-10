 #include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    double length, width;
    // 读入长方形的长和宽
    cin >> length >> width;
    // 计算周长与面积
    double perimeter = 2 * (length + width);
    double area = length * width;
    // 设置输出保留两位小数
    cout << fixed << setprecision(2);
    // 按要求格式输出结果
    cout << "周长:" << perimeter << "米，面积:" << area << "平方米";
    return 0;
}