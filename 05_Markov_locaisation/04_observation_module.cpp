#include <algorithm>
#include <iostream>
#include <vector>

#include "helpers.h"

using std::vector;

// function to get pseudo ranges
vector<float> pseudo_range_estimator(vector<float> landmark_positions,
                                     float pseudo_position);

// observation model: calculate likelihood prob term based on landmark proximity
float observation_model(vector<float> landmark_positions,
                        vector<float> observations, vector<float> pseudo_ranges,
                        float distance_max, float observation_stdev);

int main()
{
    float observation_stdev = 1.0f;         // set observation standard deviation:
    int map_size = 25;                      // number of x positions on map
    float distance_max = map_size;          // set distance max      
    vector<float> landmark_positions{5, 10, 12, 20};
    vector<float> observations{5.5, 13, 15};

    // step through each pseudo position x (i)
    for (int i = 0; i < map_size; ++i)
    {
        float pseudo_position = float(i);

        // get pseudo ranges
        vector<float> pseudo_ranges = pseudo_range_estimator(landmark_positions,
                                                             pseudo_position);

        //get observation probability
        float observation_prob = observation_model(landmark_positions, observations,
                                                   pseudo_ranges, distance_max,
                                                   observation_stdev);
        //print to stdout
        std::cout << observation_prob << std::endl;
    }

    return 0;
}

/*********************************************
For each landmark position:
    determine the distance between each pseudo position x and each landmark position
    if the distance is positive (landmark is forward of the pseudo position) 
        push the distance to the pseudo range vector
    sort the pseudo range vector in ascending order
    return the pseudo range vector
*************************************************/
vector<float> pseudo_range_estimator(vector<float> landmark_positions,
                                     float pseudo_position)
{
    // define pseudo observation vector
    vector<float> pseudo_ranges;

    // loop over number of landmarks and estimate pseudo ranges
    for (int l = 0; l < landmark_positions.size(); ++l)
    {
        // estimate pseudo range for each single landmark
        // and the current state position pose_i:
        float range_l = landmark_positions[l] - pseudo_position;

        // check if distances are positive:
        if (range_l > 0.0f)
        {
            pseudo_ranges.push_back(range_l);
        }
    }

    // sort pseudo range vector
    sort(pseudo_ranges.begin(), pseudo_ranges.end());

    return pseudo_ranges;
}
/********************************************************************************
For each observation:
    determine if a pseudo range vector exists for the current pseudo position x
    if the vector exists, extract and store the minimum distance, element 0 of the sorted vector, 
        and remove that element (so we don't re-use it). This will be passed to norm_pdf
    else the pseudo range vector does not exist, pass the maximum distance to norm_pdf
        *maximum distance gives a low prob in gaussian distribution
    use norm_pdf to determine the observation model probability
    return the total probability
*********************************************************************************/
// calculates likelihood prob term based on landmark proximity
float observation_model(vector<float> landmark_positions,
                        vector<float> observations, vector<float> pseudo_ranges,
                        float distance_max, float observation_stdev)
{
    // initialize observation probability
    float distance_prob = 1.0f;

    // run over current observation vector
    for (int z = 0; z < observations.size(); ++z)
    {
        // define min distance
        float pseudo_range_min;

        // check, if distance vector exists
        if (pseudo_ranges.size() > 0)
        {
            // set min distance
            pseudo_range_min = pseudo_ranges[0];
            // remove this entry from pseudo_ranges-vector
            pseudo_ranges.erase(pseudo_ranges.begin());
        }
        else
        { // no or negative distances: set min distance to a large number
                //*maximum distance gives a low prob in gaussian distribution
            pseudo_range_min = std::numeric_limits<const float>::infinity();
        }

        // estimate the probability for observation model, this is our likelihood
        distance_prob *= Helpers::normpdf(observations[z], pseudo_range_min,
                                          observation_stdev);
    }
    return distance_prob;
}