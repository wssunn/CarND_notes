double goal_distance_cost(int goal_lane, int intended_lane, int final_lane,
                          double distance_to_goal)
{
    // The cost increases with both the distance of intended lane from the goal
    //   and the distance of the final lane from the goal. The cost of being out
    //   of the goal lane also becomes larger as the vehicle approaches the goal.

    // KL: keep lane
    // LCL: lane change left, LCR: Lane change right
    // PLCL: prepare lane change left, PLCR: prepare Lane change right
    //Intended lane: the intended lane for the given behavior. 
    //       For PLCR, PLCL, LCR, and LCL, this would be the one lane over from the current lane.
    //Final lane : the immediate resulting lane of the given behavior.
    //       For LCR and LCL, this would be one lane over.
    int delta_d = 2.0 * goal_lane - intended_lane - final_lane;
    double cost = 1 - exp(-(std::abs(delta_d) / distance_to_goal));

    return cost;
}

double inefficiency_cost(int target_speed, int intended_lane, int final_lane,
                         const std::vector<int> &lane_speeds)
{
    // Cost becomes higher for trajectories with intended lane and final lane
    //   that have traffic slower than target_speed.

    // lane speeds: a vector; based on traffic in that lane: {6, 7, 8, 9}.
    //Intended lane: the intended lane for the given behavior.
    //       For PLCR, PLCL, LCR, and LCL, this would be the one lane over from the current lane.
    //Final lane : the immediate resulting lane of the given behavior.
    //       For LCR and LCL, this would be one lane over.

    double speed_intended = lane_speeds[intended_lane];
    double speed_final = lane_speeds[final_lane];
    double cost = (2.0 * target_speed - speed_intended - speed_final) / target_speed;

    return cost;
}