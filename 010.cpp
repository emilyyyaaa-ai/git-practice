 # 读入长方形的长和宽，计算输出周长和面积，结果保留两位小数
def calculate_rectangle(length, width):
    '''计算长方形的周长和面积'''
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

try:
    # 处理输入
    input_data = input().split()
    if len(input_data) != 2:
        print("输入错误，请输入长方形的长和宽两个数值")
    else:
        length = float(input_data[0])
        width = float(input_data[1])
        if length <= 0 or width <= 0:
            print("输入错误，长和宽必须为正数")
        else:
            perimeter, area = calculate_rectangle(length, width)
            print(f"周长：{perimeter:.2f} 米，面积：{area:.2f} 平方米")
except ValueError:
print("输入错误，请输入有效的数字")





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