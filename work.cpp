#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
    string dish1 = "瓦罐汤";
    double price1 = 12.50;
    string dish2 = "米饭";
    double price2 = 2.00;

    cout << left << setw(10) << "菜品" << right << setw(8) << "金额" << endl;
    cout << left << setw(10) << dish1 << right << setw(8) << fixed << setprecision(2) << price1 << endl;
    cout << left << setw(10) << dish2 << right << setw(8) << fixed << setprecision(2) << price2 << endl;
    return 0;
}