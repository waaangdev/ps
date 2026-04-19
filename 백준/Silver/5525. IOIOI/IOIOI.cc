// 
#include <iostream>
#include<string>
using namespace std;
int a, b,c,d,r;
string str;

int main()
{
    cin >> a;
    cin >> b;
    c = 0;
    d = 0;
    r = 0;
    cin >> str;
    for (int i = 0; i < b; i++) {
        if (str[i] == 'I') {
            if (c == 0) {
                d += 1;
                if (d >= 1 + a * 2) {
                    r += 1;
                }
            }
            else {
                d = 1;
            }
            c = 1;
        }
        else {
            if (c == 1) {
                d += 1;
            }
            else {
                d = 1;
            }
            c = 0;
        }
    }
    cout << r;
}


