#include <iostream>
using namespace std;


int main() 
{
    int i = 5;
    {
        int i = 7;
        std::cout << i << '\n';
    }
    std::cout << i << '\n';
    return 0;
}
