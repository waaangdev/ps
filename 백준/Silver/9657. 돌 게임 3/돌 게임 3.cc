#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>
#include <deque>
#include <cmath>

using namespace std;

int a;
int b[] = { 0,1,0,1,1,1,1 };


int main() {
    cin >> a;
    if (b[a%7] == 1) {
        cout << "SK";
    }
    else {
        cout << "CY";
    }
    
}