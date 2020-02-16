//
//  main.cpp
//  Module3HW
//
//  Created by Tierra Duffield on 2/23/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    // insert code here...
    int base = 2;
    int exp = 8;
    int value = base;
    
    for (int i = 1; i < exp; i++) {
        value = value * base;
    }
    std::cout << "The result is: " + std::to_string (value) << std::endl;
    return 0;
};
