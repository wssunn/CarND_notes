#include <iostream>
#include <vector>
#include "Dense"

using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::cout;
using std::endl;
using std::vector;

int main()
{
    vector<VectorXd> estimations;

    // the input list of estimations
    VectorXd e(4);
    e << 1, 1, 0.2, 0.1;
    estimations.push_back(e);
    e << 2, 2, 0.3, 0.2;
    estimations.push_back(e);
    e << 3, 3, 0.4, 0.3;
    estimations.push_back(e);

    for (int row=0; row<estimations.size(); ++row){
        cout << "\n" << estimations[row] << endl;
    }

    return 0;

}
