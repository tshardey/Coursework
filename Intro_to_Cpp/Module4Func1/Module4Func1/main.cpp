//
//  main.cpp
//  Module4Func1
//
//  Created by Tierra Duffield on 3/23/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>
#include <sstream>



int getExp(int base, int exp)
{
    int finalValue{0};
    if (exp < 0)
    {
        std::cout << "This function does not allow negative exponent values" << std::endl;
        finalValue = NULL;
    }
    else if (exp == 0)
    {
        finalValue = 1;
    }
    else
    {
        int value = base;
        for (int i = 1; i < exp; i++)
        {
            value = value * base;
        finalValue = value;
        }
    }
    return finalValue;
}

double getSin(double opp, double hyp){
    double sine = opp/hyp;
    return sine;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int runExp = getExp(4,4);
    std::cout << "The result is: " + std::to_string (runExp) << std::endl;
    int runExpTwo = getExp(2,0);
    std::cout << "The result is: " + std::to_string (runExpTwo) << std::endl;
    int runExpThree = getExp(2,-3);
    std::cout << "The result is: " + std::to_string (runExpThree) << std::endl;
    
    double runSin = getSin(1, 2);

    std::cout << runSin << std::endl;
    
    return 0;
}

