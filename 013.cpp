#include <iostream>
using namespace std;

void calculateTicket(int total_ticket, int per_need, int &count, int &remaining) {
    count = total_ticket / per_need;
    remaining = total_ticket % per_need;
}

int main() {
    int total_ticket, per_need;
    cout << "请输入餐券总数: ";
    cin >> total_ticket;
    cout << "请输入每份套餐所需餐券数: ";
    cin >> per_need;

    if (per_need <= 0) {
        cout << "输入不合法：每份套餐所需餐券数必须为正整数！" << endl;
        return 1;
    }
    if (total_ticket < 0) {
        cout << "输入不合法：餐券总数不能为负数！" << endl;
        return 1;
    }

    int count, remaining;
    calculateTicket(total_ticket, per_need, count, remaining);

    cout << "可兑换套餐:" << count << " 份，剩余餐券:" << remaining << " 张" << endl;
    return 0;
}