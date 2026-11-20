#include <iostream>
#include <string>
using namespace std;

class Car{
private:
    string brand;
    int speed;
public:
    Car(string b, int s = 0){
        brand = b;
        speed = s;
    }
    void speed_up(int n){
        speed += n;
        
    }
    void show(){
        cout <<"当前品牌：" << brand <<"当前速度" << speed <<endl;
    }
};
int main(){
    Car c("BMW")
    c.speed_up(30);
    c.show();
    c.speed_up(20);
    c.show();
    return 0;
}