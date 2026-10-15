#include  <iostream>
using namespace std;

int main()
{
    int total;
    int memberFlag;
    cin >> total >> memberFlag;      //是会员填1，不是填2
    

    int payable = total;
    int giftFlag = 0;          //输入


    if (total >= 30)
    {
        payable -= 5;
    }
    if (total >= 30 && memberFlag == 1)
    {
        giftFlag += 1;
    }

    cout << "应付金额："<< payable << endl;
    cout << "赠送小料："<< giftFlag << endl;
    cout << "祝您用餐愉快" << endl;     //输出


    return 0;




}

