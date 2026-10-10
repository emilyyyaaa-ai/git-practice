#include <iostream>
using namespace std;

int main()
{
    int score[5] = {88, 92, 79, 95, 86};
    int maxScore = score[0];
    for (int i = 1; i < 5; i++)
    {
        if (score[i] > maxScore)
        {
            maxScore = score[i];
        }
    }
    cout << "最高分是: " << maxScore << endl;
    return 0;
}