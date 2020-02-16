//
//  main.cpp
//  ControlStatements
//
//  Created by Tierra Duffield on 2/22/16.
//  Copyright © 2016 Tierra Duffield. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::string response;
    if (response == "connection_failed")
    {
        // Block of code executes if the value of the response variable is "connection_failed".
    }
    else
    {
        // Block of code executes if the value of the response variable is not "connection_failed".
    }
    
    std::string responsed;
    if (responsed == "connection_failed")
    {
        // Block of code executes if the value of the response variable is "connection_failed".
    }
    else if (responsed == "connection_error")
    {
        // Block of code executes if the value of the response variable is "connection_error".
    }
    else
    {
        // Block of code executes if the value of the response variable is neither above responses.
    }
    
    char resp = 'y';
    switch (resp)
    {
        case 'y':
            // Block of code executes if the value of response is y.
            break;
        case 'Y':
            // Block of code executes if the value of response is Y.
            break;
        case 'n':
            // Block of code executes if the value of response is n.
            break;
        default:
            // Block executes if none of the above conditions are met.
            break;
    }
    using namespace std;
    {
        int i = 1, j = 2;
        cout << ( i > j ? i : j ) << " is greater." << endl;
    }
    
    char responsend = 'n';
    if (responsend == 'y' || responsend == 'Y')
        cout << "Positive response received" << endl;
        cout << "Your progress has been saved" << endl;
        
        cout << "You did not choose y or Y" << endl;
    cout << "Your progress has not been saved" << endl;
    
    string respo;
    cout << "Enter menu choice " << endl << "More" << endl << "Quit" << endl;
    cin >> respo;
    
    while (respo != "Quit")
    {
        // Code to execute if Quit is not entered
        
        // Prompt user again with menu choices until Quit is entered
        cout << "Enter menu choice " << endl << "More" << endl << "Quit" << endl;
        cin >> respo;
    }

    string Response;
    
    do
    {
        cout << "Enter menu choice " << endl << "More" << endl << "Quit" << endl;
        cin >> Response;
        
        // Process the data.
        
    } while (Response != "Quit");
    
    // nested loops
    bool alternate = true;
    
    for (int x = 0; x < 8; x++)
    {
        for (int y = 0; y < 4; y++)
        {
            if (alternate)
            {
                cout << "X ";
                cout << "O ";
                
            }
            else
            {
                cout << "O ";
                cout << "X ";
                
            }
        }
        alternate = !alternate;
        
        cout << endl;
    }
    
    return 0;
}

