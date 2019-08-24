#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> myvec = {5, 6, 7, 3, 2};

    // min_element is in <algorithm>
    // min_element return an iterator of POINTER to min_element
    vector<int>::iterator best_number = min_element(begin(myvec), end(myvec));
    int best_idx = distance(begin(myvec), best_number);
    cout << best_idx << endl;
    cout << myvec[best_idx] << endl;

    return 0;
}