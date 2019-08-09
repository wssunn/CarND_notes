#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<float>> grid;

grid matrixsum(grid matrix1, grid matrix2){
  grid sum_matrix (matrix1.size(), vector<float>(matrix1[0].size(), 0));
  for (int row=0; row < matrix1.size(); ++row){
    for (int column=0; column < matrix1[0].size(); ++column){
      sum_matrix[row][column] = matrix1[row][column] + matrix2[row][column];
    }
  }
  return sum_matrix;
}

void matrixprint(grid inputmatrix){
  for (int row=0; row<inputmatrix.size(); ++row){
    for (int column=0; column<inputmatrix[0].size(); ++column){
      cout << inputmatrix[row][column] << " ";
    }
    cout << "\n";
  }
  cout << endl;
}

int main(){
  grid matrix1(5, vector<float>(3, 2));
  grid matrix2(5, vector<float>(3, 25));
  grid matrixresult;

  matrixresult = matrixsum(matrix1, matrix2);
  matrixprint(matrixresult);

  return 0;
}
