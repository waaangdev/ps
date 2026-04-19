#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a,b,c,inp,r,x;


int main() {
	cin >> a >> b;
	cin >> c;
	r = 0;
	x = 1;
	b -= 1;
	for (int i = 0; i < c; i++) {
		cin >> inp;
		if (inp < x) {
			r += x - inp;
			x = inp;
		}
		else if (inp > x+b) {
			r += inp-(x+b);
			x = inp - b;
		}
		//cout << x<<"a\n";
	}
	cout << r;
}
