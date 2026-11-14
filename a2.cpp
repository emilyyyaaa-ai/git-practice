 #include <iostream>
using namespace std;

// 递归计算加权和：n为当前剩余编码，weight为当前位的权重（默认从1开始），current_sum为已累加的加权和
long long calculate_weighted_sum(long long n, int weight = 1, long long current_sum = 0) {
    // 编码为0时直接返回当前累加的加权和
    if (n == 0) {
        return current_sum;
    }
    int digit = n % 10;
    // 切换下一位权重
    int next_weight = (weight == 1) ? 2 : 1;
    // 递归处理剩余位数，累加当前位的乘积
    return calculate_weighted_sum(n / 10, next_weight, current_sum + digit * weight);
}

int main()
 {
    int q;
    cin >> q;
    // 循环处理q次查询，idx从1开始
    for (int idx = 1; idx <= q; idx++) {
        long long n;
        cin >> n;
        long long weighted_sum = calculate_weighted_sum(n);
        int check_code = weighted_sum % 10;
        // 输出时用空格分隔三个值
        cout << idx << " " << weighted_sum << " " << check_code << endl;
    }
    return 0;
}    