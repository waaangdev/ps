#include <iostream>
#include <string>
#include <array>
#include <map>
#include <list>

using namespace std;
int a,max_,maxi;
double r;
array<int, 100000> li;

int main() {
	max_ = 0;
	r = 0;
	cin >> a;
	for (int i = 0; i < a; i++) {
		cin >> li[i];
		if (max_ < li[i]) {
			max_ = li[i];
			maxi = i;
		}
	}
	r = (double)max_;
	for (int i = 0; i < a; i++) {
		if (i != maxi) {
			r += (double)li[i] /2;
		}

	}
	cout << r;
}
