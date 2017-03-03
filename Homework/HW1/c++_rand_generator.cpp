// Jacob McKenna
// CS680 Advanced Discrete Event Simulations
// Assignment 1
// This assignment requires the implementation of the Linear
// Congruential Method and five different test variable sets.
// The Kolmogorov Smirnov, mean, variance, and auto correlation tests.
// These will also be applied to at least three different PRNGs.

#include <iostream>
#include <random>
#include <vector>
#include <numeric>
#include <functional>
#include <math.h>
#include <fstream>


using namespace std;

int main() {

    vector<int> testSetOne;
    
    srand((unsigned)time(0));
    float temp;
    
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    
    std::minstd_rand0 generator (seed);  // minstd_rand0 is a standard linear_congruential_engine
    std::cout << "Random value: " << generator() << std::endl;
    
    for (int i = 0; i < 10000; i++){
        
        testSetOne.push_back(generator());
        
    }
    
    for(int i = 0; i < 1000; i++)
    cout << testSetOne[i] << endl;
    
    
    sort(testSetOne.begin(), testSetOne.end());
    
    ofstream randFile;
    randFile.open("prngNums.txt");
    
    for(int i=0; i<testSetOne.size(); i++)
        randFile << testSetOne[i] << " ";
    
    
    randFile << endl;

    
    randFile.close();
    
    
    
    
    

    

    return 0;
}
