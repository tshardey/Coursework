//
//  main.cpp
//  Module4
//
//  Created by Tierra Duffield on 2/29/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    // Determining scope
    int total = 0;
    for(int i = 1; i <= 10; i++)
    {
        total += i;
        std::cout << "Current value of i is " << i << &std::cout;
    }
    std::cout << "The sum of the numbers 1 to 10 is " << total << std::endl;
    
    // Declaring a Class
    class Rectangle
    {
    public:
        int _width;
        int _height;
    };
    
    Rectangle outer;
    Rectangle inner;
    
    outer._width = 10;
    outer._height = 10;
    
    inner._width = 5;
    inner._height = 5;
    
}

// Two functions can have the same name as long as the program will be able to tell the difference.
int Sum(int x, int y)
{
    return x + y;
}

// Having a different number of peramiters is a good way to ensure the program will be able to differentiate them.

int Sum(int x, int y, int z)
{
    return x + y + z;
}

int result = Sum(3, 4);

// Inline functions avoid the overhead associated with traditional function calls.
// A swap function takes two variables and swaps their values.

inline void swap(int & a, int & b)
{
    int temp = a;
    a = b;
    b = temp;
}

// Traditional method that results in a function call
// void swap(5, 6);

// Using an inline function call, the compiler converts the previous line to this
// int temp = a;
// a = b;
// b = temp;

