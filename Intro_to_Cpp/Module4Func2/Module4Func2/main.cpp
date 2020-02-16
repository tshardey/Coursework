//
//  main.cpp
//  Module4Func2
//
//  Created by Tierra Duffield on 3/23/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>
#include <vector>
#include <array>


int avgArray(std::vector<int> array){
    double totalArray{0};
    double arraySize = array.size();
    for (int i = 0; i < arraySize ; i++) {
        totalArray += array[i];
    }
    double finalAvg = totalArray/arraySize;
    std::cout << finalAvg << std::endl;
    return finalAvg;
}

int main(int argc, const char * argv[]) {
    std::vector<int> myArray{1, 2, 3, 4, 5};
    avgArray(myArray);
    return 0;
}
