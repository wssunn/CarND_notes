#ifndef KALMAN_FILTER_H_
#define KALMAN_FILTER_H_
#include "Dense"

using Eigen::MatrixXd;
using Eigen::VectorXd;

class KalmanFilter {
   public:
      KalmanFilter();
      virtual ~KalmanFilter();

      void Predict();
      void Update(const VectorXd &z);

      VectorXd x_; // state vector
      MatrixXd P_; // state covariance matrix
      MatrixXd F_; // state transistion matrix
      MatrixXd Q_; // process covariance matrix
      MatrixXd H_; // measurement matrix
      MatrixXd R_; // measurement covariance matrix
};

#endif  // KALMAN_FILTER_H_
