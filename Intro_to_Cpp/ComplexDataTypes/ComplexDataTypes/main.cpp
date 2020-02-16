//
//  main.cpp
//  ComplexDataTypes
//
//  Created by Tierra Duffield on 2/21/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    int arrayName[10];
    int oldNumbers = arrayName[2];
    std::cout << oldNumbers << std::endl;
    int arrayNameTwo[] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) {
        int number = arrayNameTwo[i];
        std::cout << number << std::endl;
    };
    
    char isAString[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    char isNotAString[5] = {'H', 'e', 'l', 'l', 'o'};
    std::cout << isAString << std::endl;
    std::cout << isNotAString << std::endl;
    
    char stringLit[6] = "Hello";
    char isAnotherString[] = "Array size is inferred";
    std::cout << stringLit << std::endl;
    std::cout << isAnotherString << std::endl;
    
    using namespace std;
    string myString = "Hello!";
    std:: string myNewString = "Less typing";
    
    struct coffeeBean
    {
        string name;
        string country;
        int strength;
        
    };
    
    coffeeBean myBean = {"Strata", "Columbia", 10};
    coffeeBean newBean;
    newBean.name = "Flora";
    newBean.country = "Mexico";
    newBean.strength = 9;
    cout << "Coffee bean " + newBean.name + " is from " + newBean.country << endl;
    
    union numbericUnion
    {
        int intValue;
        long longValue;
        double doubleValue;
    };
    
    numbericUnion myUnion;
    myUnion.intValue = 3;
    cout << myUnion.intValue << endl;
    myUnion.doubleValue = 4.5;
    cout << myUnion.doubleValue << endl;
    cout << myUnion.intValue; cout << endl;
    
    enum Day { Sunday = 1, Monday, Tuesday, Wednesday, Thursday, Friday, Staturday };
    Day payDay;
    payDay = Thursday;
    cout << payDay << endl;
    
    
    return 0;
}


