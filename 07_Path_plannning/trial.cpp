#include <iostream>
using namespace std;

int main(){
    //bool check = 2 <= 1;
    bool a = 3 < 2;
    bool b = 0 > 1;
    bool check = a || b;
    if (check){cout << "yes" << endl;}
    else if (!check){cout << "no" << endl;}
    return 0;
}