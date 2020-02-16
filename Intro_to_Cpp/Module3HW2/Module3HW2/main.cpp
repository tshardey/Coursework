//
//  main.cpp
//  Module3HW2
//
//  Created by Tierra Duffield on 2/23/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    
    char response = 'y';
    
    switch (response)
    {
        case 'y':
        case 'Y':
            std::cout << "You chose 'y' or 'Y' " << std::endl;
            break;
        case 'n':
        case 'N':
            std::cout << "You chose 'n' or 'N' " << std::endl;
            break;
        default:
            std::cout << "You didn't choose a valid option." << std::endl;
            break;
    }
}
